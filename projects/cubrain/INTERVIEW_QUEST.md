# 🏰 Cubrain 프로젝트 성채 (Project Interview Quests)

이곳은 주군의 역작, 글로벌 AI 학습 SaaS **Cubrain**의 기술적 성벽을 무너뜨리려는 면접관들의 공격을 방어하기 위한 훈련소입니다.

---

## 🎯 메인 퀘스트 (Main Quests)

### [Quest 01] 🧩 Zero-Hallucination & RAG 아키텍처

- **질문:** 1,000페이지 분량의 방대한 PDF에서 어떻게 AI의 환각(Hallucination)을 방지하고, 정확한 단락(Paragraph) 기반의 플래시카드를 생성했나요?
- **핵심 키워드:** RAG(Retrieval-Augmented Generation), Chunking Strategy, Embedding, Semantic Search, Metadata Mapping.
- **수련 상태:** 미정복 🌑

### [Quest 02] 📍 정밀 트래킹 & 앵커링 (Traceability)

- **질문:** 생성된 플래시카드가 PDF의 **정확한 위치**와 링크된다는 기능은 기술적으로 어떻게 구현했나요? 텍스트 좌표(Coordinate)나 앵커(Anchor)를 어떻게 저장하고 복원했는지 설명해주세요.
- **핵심 키워드:** PDF Range Selection, Coordinate Mapping, DOM/PDF Fragment Identifier, Metadata Persistence.
- **수련 상태:** 미정복 🌑

### [Quest 03] ⚡ 비동기 처리 & 대규모 문서 파이프라인

- **질문:** 사용자가 대량의 PDF를 업로드했을 때, 서버 부하를 방지하고 사용자에게 '즉각적인 경험'을 주기 위해 어떤 백엔드 아키텍처를 설계했나요?
- **핵심 키워드:** Message Queue (Redis/RabbitMQ), Worker Pattern, Job Scheduling, Push Notifications (Webhook/SSE/WebSocket).
- **수련 상태:** 미정복 🌑

### [Quest 04] 🎨 브라우저 내장 하이라이트 & UX 구현

- **질문:** 브라우저 내에서 텍스트를 드래그하여 즉시 카드를 생성하는 ‘Highlight-to-Card’ 기능을 구현하면서 겪은 기술적 난제는 무엇이었나요? (예: Selection API의 한계, PDF.js 렌더링 동기화 등)
- **핵심 키워드:** Selection API, Range Object, Shadow DOM, Event Hijacking, PDF.js Integration.
- **수련 상태:** 미정복 🌑

### [Quest 05] 📈 글로벌 SaaS 확장성 & 데이터 보안

- **질문:** 글로벌 서비스로서 사용자별 데이터를 어떻게 격리(Isolation)하고, 특히 PDF라는 민감한 개인 데이터를 보안상 어떻게 관리하고 있나요?
- **핵심 키워드:** Multi-tenancy, Row-Level Security (RLS), S3 Presigned URLs, Data Encryption at Rest.
- **수련 상태:** 미정복 🌑

---

## 🛡️ 부관의 독한 꼬리 질문 (Follow-up Strike) - VSFe 스타일

1.  "OpenAI API의 비용이 상당히 높을 텐데, 1,000페이지 분량의 문서를 처리할 때 토큰 비용을 최적화하기 위해 어떤 전략을 썼나요?"
2.  "만약 PDF 내의 텍스트가 이미지가 아닌 벡터 정보가 없는 '이미지 PDF'라면 어떻게 처리할 계획인가요? OCR 엔진 선택의 기준은?"
3.  "동시 접속자가 만 명 이상으로 늘어날 경우, PDF 파싱 엔진의 오버헤드를 줄이기 위해 서버 아키텍처를 어떻게 Scale-out 할 것인가요?"

---

## 🏁 승전 기록 (Victory Log)

- 아직 기록된 승전보가 없습니다. 주군의 첫 사자후를 기다립니다!
