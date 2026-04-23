# 🏎️ sbb_board 사고의 공방 (Public Analysis)

이곳은 **sbb_board**의 백엔드 성능 지표와 JPA 최적화 성과를 기록하는 공용 공간입니다.

---

## 🚀 전술적 전과 (Performance Intel)

> **"대규모 트래픽 환경에서의 지연 시간 98.9% 개선"**

| 데이터 규모  | 개선 전 (Fetch Join) | 개선 후 (Optimization) | 성능 개선율 |
| :----------- | :------------------- | :--------------------- | :---------- |
| **10,000건** | 6,506ms              | **70ms**               | **98.9%**   |

### 🔍 핵심 인사이트

1.  **I/O 병목 가시화:** Join으로 인한 지수적 데이터 폭증(Cartesian Product)을 식별하고 해결.
2.  **연산 분산 전략:** DB 부하를 애플리케이션 계층으로 효율적으로 분산하여 전체 시스템 처리 용량(Throughput) 확보.

---

## 🛠️ 적용 기술 (Tech Stack)

- **Framework:** Spring Boot, Spring Data JPA
- **Optimization:** Custom Query Design, In-memory Data Transformation

---

## 🛡️ 부관의 조언

"주군, 이곳에서는 숫자로 승부하십시오. 6,500ms가 70ms로 변하는 마법 같은 지표가 면접관의 시선을 사로잡을 것입니다."
