# 📊 sbb_board: 백엔드 최적화 (Backend & JPA Mastery)

이곳은 서버의 심장, **sbb_board** 프로젝트의 N+1 문제와 DB 쿼리 최적화 전술을 기록하는 공간입니다.

---

## 🚀 전술적 전과 (Performance Intel) - 데이터 규모별 정밀 분석

> **"수면 위로 드러난 Cartesian Product의 참상과 Semi Join의 압도적 효율"**

| 데이터셋     | Semi Join   | Fetch Join          | Lazy Loading (N+1) | **성능 개선율** |
| :----------- | :---------- | :------------------ | :----------------- | :-------------- |
| **1,000건**  | 20ms (40개) | 683ms (14,277개)    | 75ms (309개)       | **97.1%**       |
| **5,000건**  | 16ms (40개) | 1,430ms (68,125개)  | 54ms (304개)       | **98.9%**       |
| **10,000건** | 70ms (40개) | 6,506ms (136,518개) | 119ms (274개)      | **98.9%**       |

### 🔍 핵심 인사이트 (Core Insights)

1.  **스케일 효율성 (Scale Efficiency):** 데이터 증가에도 Semi Join은 항상 동일한 엔티티(40개)만 로드하여 압도적 안정성 유지.
2.  **Cartesian Product의 참상:** Fetch Join은 데이터 10배 증가 시 로드량이 **3,413배** 폭증하며 성능이 궤멸적(6.5초)으로 하락.
3.  **역설적 현상 (Lazy Loading vs Fetch Join):** 5,000건 기준, 오히려 21번의 쿼리를 던지는 **Lazy Loading(54ms)**이 단일 쿼리인 **Fetch Join(1,430ms)**보다 약 26배 빠름. 이는 조인으로 불어난 거대 데이터셋 전송 비용이 쿼리 왕복 비용보다 훨씬 치명적임을 시사.

---

## 🛠️ 백엔드 성능 퀘스트 (Technical Quests)

### [Quest 01] ⚡ JPA N+1 문제와 근본적 해결책

- **질문:** 게시판 애플리케이션(sbb_board)에서 빈번하게 발생하는 **N+1 문제**의 정의와, 이를 **semi join + StreamAPI**라는 독특한 조합으로 해결하게 된 배경과 이유는 무엇인가요?
- **핵심 키워드:** N+1 Problem, Lazy/Eager Loading, Proxy, Join Strategy, Bulk Fetching.
- **수련 상태:** 미정복 🌑

### [Quest 02] 🧩 Semi-join vs Fetch Join (Trade-off)

- **질문:** 왜 일반적인 `Fetch Join`이나 `@EntityGraph`를 쓰지 않고 **semi join** 방식을 선택했나요? 이 방식이 데이터 중복(Cartesian Product) 방지나 메모리 효율 측면에서 가졌던 이점은 무엇이었나요?
- **핵심 키워드:** Semi-join (EXISTS/IN), Cartesian Product, Distinct, In-memory Processing.
- **수련 상태:** 미정복 🌑

### [Quest 03] 🌊 StreamAPI 기반 데이터 정제 및 최적화

- **질문:** DB에서 가져온 데이터를 **Java StreamAPI**를 통해 가공할 때 발생했던 성능상의 이점과 혹시 모를 오버헤드는 무엇이었나요? Stream의 지연 연산(Lazy Evaluation)이 쿼리 결과 처리에 어떤 도움을 주었는지 설명해주세요.
- **핵심 키워드:** StreamAPI, Parallel Stream, Lazy Evaluation, Functional Interface.
- **수련 상태:** 미정복 🌑

---

## 🛡️ 부관의 독한 꼬리 질문 (Follow-up Strike) - 시니어 엔지니어링

1. "Semi-join 방식은 대량의 데이터를 `IN` 절에 넣을 때 DB 버퍼 오버플로우나 쿼리 길이 제한 문제가 생길 수 있습니다. 이 부분을 어떻게 Batch Size 설정으로 해결했나요?"
2. "`fetchJoin`은 1:N 관계에서 페이징 처리가 불가능하다는 고질적인 문제가 있는데, 주군의 방식(semi join + streamAPI)은 이 페이징 문제를 어떻게 우아하게 해결했습니까?"
3. "StreamAPI를 사용하면 CPU 연산량이 늘어날 수 있는데, DB의 `Group By`나 `Aggregations`로 처리하는 대신 애플리케이션 레벨에서 처리한 특별한 이유(비즈니스 로직의 복잡성 등)가 있나요?"

---

## 🏁 승전 기록 (Victory Log)

- 아직 기록된 승전보가 없습니다. 주군의 첫 사자후를 기다립니다!
