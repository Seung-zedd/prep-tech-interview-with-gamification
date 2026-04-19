# 📜 Database Quest: 대규모 트래픽 최적화

## ⚔️ 메인 퀘스트 (Main Quest)

### [Quest 01] ⚡ Disk I/O 방어와 인덱스 전략

- **질문:** 대규모 서비스에서 JPA만 사용했을 때 발생하는 성능 병목의 원인(Why)과, 이를 **커버링 인덱스(Covering Index)**를 통해 해결하는 구체적인 원리를 설명해주세요.
- **핵심 키워드:** Disk I/O, Clustering Index, Secondary Index, Covering Index (Index Full Scan vs Table Full Scan).
- **수련 상태:** 미정복 🌑

### [Quest 02] 🌪️ 동시성 부하와 Redis 방어망

- **질문:** 수만 명의 유저가 동시에 접근할 때, 단순히 인덱스 튜닝만으로 해결할 수 없는 병목 현상은 무엇이며, **Redis의 Look Aside와 Write Behind 패턴**을 각각 어떤 상황에 도입해야 하는지 트레이드오프와 함께 설명해주세요.
- **핵심 키워드:** Connection Pool Exhaustion, Row Lock, Atomic Operation (INCR), Look Aside, Write Behind (Batch Update).
- **수련 상태:** 미정복 🌑

---

## 🛡️ 부관의 독한 꼬리 질문 (Follow-up Strike)

1. "커버링 인덱스를 구성할 때 컬럼의 순서(Ordered Composite Key)가 중요한 이유는 무엇이며, 만약 순서가 어긋났을 때 인덱스는 어떻게 동작하나요?"
2. "Redis를 `Write Behind`로 쓰다가 캐시 서버가 불의의 사고로 다운되면 데이터 정합성 문제가 생깁니다. 이를 현업에서 어떻게 보완하거나 감수하나요?"
3. "DB 커넥션 풀이 고갈되었을 때, 애플리케이션 레벨(Spring)에서 확인할 수 있는 대표적인 에러 로그나 징후는 무엇인가요?"
