# 🧠 사고의 단련장: Database

이곳은 데이터베이스 관련 질문에 대한 사고 과정을 기록하는 성소입니다.

---

## 📈 사고 진화 기록 (Evolution Log)

1.  **[대규모 트래픽] [JPA → Index → Redis] 성능 병목과 검색 최적화**
    - **전술 지도:** [THOUGHT_WORKSHOP.md](./01_large_traffic_search/THOUGHT_WORKSHOP.md)

---

## 🛡️ 오답 및 맹점 보강 (Weak Point Analysis)

| 퀘스트 (전장)             | 실수 내용               | 보완할 핵심 키워드         | 다시 적어보는 모범 답안                                                                                                 |
| :------------------------ | :---------------------- | :------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **사이버다임 필기 (Q18)** | GROUP BY 문법 오해      | `Non-aggregated Column`    | "에러는 `NAME`입니다. `GROUP BY` 절에 없는 일반 컬럼은 집계 함수 없이 단독으로 SELECT 할 수 없습니다."                  |
| **사이버다임 필기 (Q6)**  | 계층형 쿼리 미숙지      | `CONNECT BY`, `START WITH` | "부모-자식 관계를 타는 쿼리 문법입니다. `START WITH`는 시작점, `CONNECT BY PRIOR 부모ID = 자식ID`는 하향식 전개입니다." |
| **사이버다임 필기 (Q12)** | 트랜잭션 격리 수준 암기 | `Isolation Level`          | "Read Committed(오라클 기본), Repeatable Read, Serializable 4단계와 이상현상(Dirty/Phantom) 매칭."                      |

---

## 🖼️ 사고의 시각화 (Tactical Diagrams)

![사이버다임 필기 노트 (DB/Java 통합)](../assets/images/database/writing_test/q_paper_p2.png)
