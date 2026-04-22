![Cubrain 비동기 아키텍처](../../assets/images/projects/cubrain/q1_async_architecture.png)

# 📚 기술적 분석: PDF 데이터 적재 및 플래시카드 합성 엔진

본 분석은 `cubrain` 프로젝트의 PDF 적재 시스템의 엔드 투 엔드 흐름을 다룹니다. 초기 `POST` 요청부터 비동기 AI 처리, 그리고 실시간 SSE(Server-Sent Events) 업데이트까지의 과정을 기술적으로 복기합니다.

---

## 1. 요청 처리 및 보안 (PDF 업로드 컨트롤러 계층)

### 핵심 설계 관점: Multipart Handling & Disk Spooling

- **Maximum Memory Efficiency (Disk Spooling)**: 기존의 메모리 상주 방식에서 로컬 디스크 스풀링(`Local Disk Spooling`) 모델로 업그레이드하여 메모리 효율성을 극대화했습니다.
- **🛡️ OOM-Safe PDF Ingestion**: `MultipartFile`을 수신 즉시 대규모 힙(Heap) 메모리에 적재하지 않고, 안전한 서버 임시 경로(`Path`)로 변환하여 저장합니다. 이를 통해 초대형 문서 처리 시에도 서버가 `OutOfMemoryError (OOM)`로 다운되는 것을 원천 봉쇄했습니다.
- **On-Demand Loading**: PDF 엔진이 문서 전체가 아닌 필요한 부분만 디스크에서 로드하여 처리하므로, 런타임 메모리 풋프린트(Memory Footprint)를 획기적으로 줄였습니다.
- **Zero-Waste Lifecycle**: 작업 완료 후 혹은 에러 발생 시에도 임시 파일이 서버에 남지 않도록 보장하는 `garbage-proof` 클린업 메커니즘(`Files.deleteIfExists`)을 구현하였습니다.

### 💡 면접 핵심 포인트: 리팩토링 히스토리 (Troubleshooting)

> **Q: "왜MultipartFile을 직접 처리하지 않고 디스크 스풀링 방식을 선택했나요?"**  
> _A: 초기에는 `MultipartFile`의 `InputStream`을 직접 파라미터로 넘겨 사용했습니다. 하지만 `JobManager`를 통한 비동기 처리 과정에서 **스트림 고갈(Stream Exhaustion)** 문제가 발생했습니다. 스트림은 일회성이기 때문에 첫 번째 검증 단계 이후 실제 카드 생성 잡(Job)이 실행될 때 데이터를 읽지 못하는 현상이 있었습니다._
>
> **Q: "그럼 메모리에 byte[]로 담아두면 되지 않았나요?"**  
> _A: 네, 해결을 위해 잠시 `byte[]`로 변환하여 메모리에 적재하는 시도를 했습니다. 하지만 이 경우 대용량 PDF가 업로드되거나 동시 사용자가 늘어날 때 **Heap 메모리 점유율이 급증하여 OOM이 발생**하는 더 큰 안정성 결함이 발견되었습니다. 결국 안정성과 성능의 트레이드오프를 고려하여, 디스크를 버퍼로 활용하고 필요한 시점에만 로드하는 현재의 구조로 리팩토링하여 메모리 효율과 동시성 문제를 모두 해결했습니다._
>
> **💡 시니어급 통찰 (CS Fundamental Link):**
> 위 리팩토링 결정은 운영체제의 **가상 메모리(Virtual Memory) 관리 기법인 [Swap 영역(Swap Area)](../../os/01_virtual_memory/THOUGHT_WORKSHOP.md#🖼️-사고의-시각화-memory--storage-hierarchy)**의 원리를 애플리케이션 레이어에서 구현한 것과 같습니다. 메모리라는 한정된 자원을 효율적으로 운영하기 위해 디스크를 보조 저장소로 활용하고, **Demand Paging** 방식을 모방하여 필요한 시점에만 데이터를 로드함으로써 시스템의 안정성(Availability)을 극대화했습니다. (참조: [사고의 시각화: Memory & Storage Hierarchy](../../os/01_virtual_memory/THOUGHT_WORKSHOP.md#🖼️-사고의-시각화-memory--storage-hierarchy))\_

---

## 2. Asynchronous Lifecycle 및 상태 관리

### 데이터 흐름

1.  **Request Thread**: 고유한 `jobId`를 생성하고 비동기 실행(`CompletableFuture`)을 시작한 뒤, 즉시 클라이언트에게 `jobId`를 반환하여 응답 대기 시간을 최소화합니다.
2.  **Background Thread**: 반환된 파일 정보를 바탕으로 핵심 도메인 로직(플래시카드 생성 등)을 수행합니다.
3.  **SSE Updates**: 전체 작업 관리자가 진행 상황(`PROGRESS`)과 완료(`COMPLETE`) 이벤트를 모든 리스너에게 브로드캐스트합니다.

### 🏗️ Architectural Strength

작업 관리 계층은 백그라운드 처리 스레드와 통신 프로토콜(SSE) 사이의 **Stateful Communication Layer** 역할을 합니다. 이를 통해 비즈니스 로직과 통신 프로토콜을 완전히 분리(Decoupling)하여 유지보수성을 높였습니다.

---

## 3. SSE와 "100% Stuck" Race Condition 해결

### Critical Finding: 실행 속도와 네트워크 지연의 불일치

이는 내부 CPU/스레드 실행 속도와 외부 네트워크 지연 시간의 차이로 인해 발생하는 고전적인 동시성 버그였습니다.

- **내부 실행 속도**: 작은 파일이나 캐싱된 응답의 경우, 백그라운드 스레드는 밀리초 단위로 작업을 완료합니다.
- **네트워크 지연**: 클라이언트 브라우저는 `POST` 응답을 받고 자바스크립트를 실행한 뒤 SSE 연결(`GET`)을 맺기까지 약 200ms~1000ms가 소요됩니다.

**Failure Sequence:**

1.  브라우저가 `POST` 응답을 수신함.
2.  백그라운드 스레드가 완료되어 `COMPLETE` 이벤트를 발생시키나, 브라우저는 아직 SSE로 연결되지 않은 상태임.
3.  브라우저가 연결되었을 때는 이미 이벤트가 지나간 후임.
4.  **UI Hangs**: 클라이언트는 100% 진행률에서 멈춘 채, 다시는 오지 않을 이벤트를 무한정 기다리게 됨.

### 🔧 "State-aware (Sticky State)" 솔루션

SSE 연결 초기화(`INIT`) 이벤트를 **State-aware** 방식으로 개편하여 해결했습니다. 단순히 스트림을 시작하는 대신, 현재 작업 상태를 즉시 확인합니다. 작업이 이미 완료되었다면 초기 핸드쉐이크 단계에서 결과를 데이터에 포함시켜 전송함으로써, 늦게 연결된 클라이언트도 상태를 동기화(Catch-up)할 수 있게 했습니다.

---

## 4. AI Strategy: Synthesis over Extraction

### Prompt Engineering 기반 지식 합성

단순한 지침 전달이 아닌, 사용자의 학습 패턴을 분석하여 AI가 최적의 결과물을 내놓도록 유도합니다.

- **Synthesis over Extraction**: 사용자가 강조하거나 중요하게 표시한 영역을 기반으로 단순히 텍스트를 추출하는 것이 아니라, "개념적 원리(Why/How)" 질문을 합성 유도하도록 설계했습니다.
- **사실 기반 검증**: 세부적인 데이터 포인트를 기반으로 객관적 사실 여부를 묻는 질문을 추출합니다.

### Efficiency vs. Quality Trade-offs

- **Grouping**: 성능과 토큰 비용을 고려하여 데이터를 페이지 단위로 그룹화하여 컨텍스트를 유지하면서 효율을 극대화했습니다.
- **Multi-tier Logic**: 사용자 계정의 등급에 따라 결과물의 정밀도와 생성 개수를 동적으로 조절하여 인프라 비용을 최적화했습니다.

---

## 5. 서비스 리소스 제어 및 정책 적용

- **인증 상태별 제한**: Unauthenticated User(게스트)와 일반/프로 사용자를 식별하여 Usage Limit 정책을 적용합니다. 이는 메모리 내 ConcurrentHashMap 관리를 통해 고성능을 유지합니다.
- **Atomic Increment**: 복수의 요청이 동시에 들어올 때 카운트 정합성을 보장하기 위해 Transaction Isolation Level을 활용하여 데이터 일관성을 유지합니다.

---

## 6. OAuth 전환 및 인증 상태 영속성 논리

### 문제 상황

소셜 로그인(Google 등)을 통해 게스트에서 정식 회원으로 전환될 때, 다음과 같은 이유로 작업 상태가 유실되는 문제가 발생했습니다.

- **렌더링 시점 차이**: 서버가 리다이렉트 페이지를 렌더링하는 시점과 브라우저에 인증 쿠키가 동기화되는 시점의 불일치.

### 해결 방안

프론트엔드에서 **Client-side Auth Sync**를 구현했습니다. 사용자 상태 변화를 감시하여, 인증이 공식적으로 확인되는 즉시 백그라운드에서 이전 작업과의 연결을 재시도합니다. 이를 통해 서버 렌더링 시점에 사용자 신원을 즉시 파악하지 못하더라도 결과물을 안정적으로 복구할 수 있습니다.

---

## 7. 프론트엔드 배포 및 캐시 제어 전략 (`vercel.json`)

### 현상: 배포 직후의 JS 번들 불일치 문제

백엔드와 프론트엔드를 모두 재배포했음에도 불구하고, 일부 사용자의 UI가 여전히 100%에서 멈추는 현상이 지속되었습니다. 이는 브라우저가 **과거 버전의 자바스크립트 번들 캐시**를 계속 사용했기 때문입니다. 구버전 번들에는 SSE Race Condition 해결 로직이 포함되어 있지 않아, 배포 직후 새 백엔드가 개선된 데이터를 보내도 프론트엔드가 이를 처리하지 못한 것입니다.

### 근본 원인: 브라우저 HTTP 캐싱 전략

Vercel 등의 CDN은 기본적으로 정적 자산에 대해 강력한 캐싱을 적용합니다. 명시적인 `Cache-Control` 헤더가 없으면 브라우저는 수 시간에서 수 일 동안 기존 파일을 재사용합니다. 특히 모든 JS 파일의 통로가 되는 `index.html`이 캐싱되면 서버에 새 코드가 올라가도 사용자는 구버전을 보게 됩니다.

---

## 🏁 기술 면접 대응 성과 요약

| 기술적 과제                  | 해결 전략                                       |
| :--------------------------- | :---------------------------------------------- |
| **Memory Efficiency**        | **Multipart Disk Spooling**을 통한 OOM 방지     |
| **Async Stability**          | JobManager 기반 **Stream Exhaustion** 문제 해결 |
| **Asynchronous Processing**  | CompletableFuture + SSE Real-time Updates       |
| **Cleanup Strategy**         | Exception Handling을 통한 강제 삭제 보장        |
| **AI Hallucination Control** | User Study Trace를 최우선 컨텍스트로 활용       |
| **SSE Race Condition**       | State-aware Handshake 적용으로 데이터 유실 방지 |
| **Deployment Reliability**   | Cache-Control 고도화 (`no-cache` / `immutable`) |

이러한 설계는 **비동기 시스템**, **자원 관리**, **사용자 가치 중심의 AI 엔지니어링**, 그리고 **프론트엔드 배포 신뢰성**에 대한 깊은 이해를 증명합니다.
