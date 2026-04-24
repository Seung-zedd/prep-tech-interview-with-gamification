# 📜 기술 면접 병법서: Database (Interview Quest Log)

---

## 🗄️ Database Checklist

- [x] RDBMS vs NoSQL
- [ ] 트랜잭션의 ACID 성질
- [x] 인덱스(Index)의 원리와 자료구조 (B-Tree, Covering Index)
- [ ] 데이터베이스 정규화(Normalization)
- [ ] Redis를 활용한 캐싱 전략 (Write Behind, Look Aside)
- [x] Oracle 특화 문법 (계층형 쿼리, NVL)
- [x] 트랜잭션 격리 수준 (Isolation Level)

---

## ⚔️ 승전 기록 (Quest Archives)

1.  **[대규모 트래픽] [성능 병목과 검색 최적화]**
    - **전장(Quest):** [INTERVIEW_QUEST.md](./01_large_traffic_search/INTERVIEW_QUEST.md)
    - **핵심 주제:** Disk I/O, Covering Index, Redis Write Behind

2.  **[실무 필기] (주)사이버다임 기술 전형 (Database)**
    - **핵심 주제:** Oracle 특화 문법, 인덱스 성능 저하, 트랜잭션 격리 수준
    - **주요 퀘스트:**
      - Q5. NVL vs NVL2 vs COALESCE 차이
      - Q6. Oracle 계층형 쿼리 (`START WITH`, `CONNECT BY`)
      - Q7. 인덱스 개념 및 인덱스를 타지 않는 경우 (컬럼 변형, LIKE 앞 % 사용)
      - Q8. ROWNUM vs ROW_NUMBER()
      - Q10. SQL 작성 원칙 (SELECT \* 지양, EXISTS 활용)
      - Q11. 대용량 데이터 타입 (CLOB vs BLOB)
      - Q12. 트랜잭션 격리 수준 4단계 및 이상 현상
      - Q15. LEFT OUTER JOIN 결과 행 개수 예측
      - Q18. GROUP BY 문법 에러 (집계되지 않은 컬럼)
    - **성과:** [Rank A-] GROUP BY 문법 및 격리 수준 세부 암기 사항에서 보정 받음.
