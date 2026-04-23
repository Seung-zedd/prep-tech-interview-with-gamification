# 🏢 (주)사이버다임 기술전형 필기 대비 전략서

## 📋 전형 정보 (Exam Info)

- **일시:** 2026-04-24(금) 10:30 ~ 11:30 (60분)
- **장소:** 사이버다임 본사 (잠실역 9번 출구)
- **형식:** 단답형 + 서술형 (샤프/지우개 지참)
- **범위:** Java(객체지향, 라이브러리, 예외, 성능), DB(전반, Oracle 특화)

---

## ⏳ [문제편] 실전 대비 모의고사

### ⚔️ [Section 1] Java 핵심 예상 문제 (단답/서술)

**Q1. 객체지향 4대 특징에 대해 서술하고, 자바에서 '다형성'을 구현하는 구체적인 예시를 기술하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q2. `String`, `StringBuilder`, `StringBuffer`의 차이점을 성능과 스레드 안전성 관점에서 설명하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q3. JVM의 메모리 영역(Runtime Data Area) 중 Stack과 Heap의 차이를 설명하고, 가비지 컬렉션(GC)의 대상이 되는 영역은 어디인지 답하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q4. Checked Exception과 Unchecked Exception의 차이를 서술하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

---

### 🏛️ [Section 2] Database & Oracle 특화 예상 문제

**Q5. Oracle에서 `NULL` 값을 처리하는 함수인 `NVL`, `NVL2`, `COALESCE`의 차이를 쓰시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q6. Oracle에서 '계층형 쿼리'를 작성할 때 사용하는 예약어들을 순서대로 나열하고 그 역할을 서술하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q7. 인덱스(Index)의 개념을 설명하고, 인덱스를 생성하더라도 성능이 개선되지 않거나 인덱스를 타지 않는 경우 2가지를 기술하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q8. Oracle의 `ROWNUM`과 `ROW_NUMBER()`의 차이점은?**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

---

### 🚀 [Section 3] 성능 튜닝 및 라이브러리 (최적화)

**Q9. 자바 성능 튜닝 시 컬렉션 프레임워크 선택 가이드 (ArrayList vs LinkedList)에 대해 설명하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q10. DB 성능 향상을 위한 SQL 작성 원칙 (Best Practice) 3가지를 기술하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

---

### 🏗️ [Section 4] 솔루션 특화 예상 문제 (Document Management context)

**Q11. 대용량 텍스트나 바이너리 데이터를 DB에 저장할 때 사용하는 데이터 타입(CLOB, BLOB)의 차이를 설명하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

**Q12. 데이터베이스의 트랜잭션 격리 수준(Isolation Level) 4가지를 나열하시오.**
(답변 작성란: **********\*\***********\_\_\_\_**********\*\***********)

---

### 💻 [Section 5] 실전 코드 실행 예측 (Code Prediction Drill)

**Q13. 다음 자바 코드의 출력 결과는?**

```java
class Parent {
    public void display() { System.out.print("Parent "); }
}
class Child extends Parent {
    public void display() { System.out.print("Child "); }
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        p.display();
    }
}
```

(정답: \_\_\_\_)

**Q14. 다음 코드에서 컴파일 에러가 발생하는 라인 번호와 그 이유는?**

```java
1: abstract class Animal {
2:     abstract void cry();
3: }
4: class Cat extends Animal {
5:     void cry() { System.out.println("Meow"); }
6: }
7: public class Test {
8:     public static void main(String[] args) {
9:         Animal a = new Animal();
10:        Animal b = new Cat();
11:    }
12: }
```

(에러 라인: \_**\_ / 사유: ****\*\*\*\*******\_\_******\*\*\*\*******)

**Q15. 다음 SQL의 실행 결과로 출력되는 행(Row)의 개수는?**

- **Table A:** (ID: 1, 2, 3)
- **Table B:** (ID: 1, 2)

```sql
SELECT A.ID
FROM TableA A LEFT OUTER JOIN TableB B ON A.ID = B.ID;
```

(정답: \_\_\_\_)

---

### 🔥 [Section 6] 정처기 실기 스타일 심화 보급 (EIP Advanced Drill)

**Q16. 다음 자바 코드의 출력 결과는?**

```java
class Counter {
    static int count = 0;
    Counter() {
        count++;
        System.out.print(count + " ");
    }
}
public class Main {
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
    }
}
```

(정답: \_\_\_\_)

**Q17. 다음 코드의 실행 결과는?**

```java
public class Main {
    public static void main(String[] args) {
        int a = 5, b = 10;
        if (a > 0 || ++b > 10) {
            System.out.print("True ");
        }
        System.out.println("b=" + b);
    }
}
```

(정답: \_\_\_\_)

**Q18. 다음 SQL에서 에러가 발생하는 부분은?**

```sql
SELECT DEPARTMENT, SUM(SALARY), NAME
FROM EMPLOYEES
GROUP BY DEPARTMENT;
```

(정답: \_\_\_\_)

---

## 📝 [해설지] (Answer Key & Senior Insights)

### ⚔️ [Section 1] Java 핵심

- **Q1. 객체지향 4대 특징 & 다형성 예시**
  - **정답:** 추상화(Abstraction), 상속(Inheritance), 다형성(Polymorphism), 캡슐화(Encapsulation).
  - **해설:** 다형성은 부모 타입 참조 변수로 자식 객체를 할당받는 능력입니다. 주군이 언급하신 **`@Qualifier`**를 통한 인터페이스 구현체 주입은 결합도(Coupling)를 낮추고 개방-폐쇄 원칙(OCP)을 준수하는 가장 실무적인 예시입니다.
- **Q2. String vs StringBuilder vs StringBuffer**
  - **정답:** String(불변/안전/연산 시 신규 객체 생성), StringBuilder(가변/빠름/Thread-unsafe), StringBuffer(가변/느림/Thread-safe).
  - **해설:** `StringBuffer`는 메서드에 `synchronized`가 붙어 있어 락(Lock)을 획득해야 하므로 성능이 떨어집니다. 주군의 필기 노트에 적힌 "새로운 객체 생성으로 인한 O(N^2) 부하" 언급은 GC 관점에서 매우 훌륭한 인사이트입니다.
- **Q3. JVM Stack vs Heap & GC**
  - **정답:** Stack(기본형 변수, 지역변수, 스레드별 독립), Heap(참조형 객체, 공유 영역, GC 대상).
  - **해설:** Stack은 메서드 종료 시 즉시 소멸하나, Heap은 GC가 결정할 때까지 유지됩니다. Stack 부족 시 `StackOverflowError`, Heap 부족 시 `OutOfMemoryError(OOM)`가 발생함을 기억하십시오.
- **Q4. Checked vs Unchecked Exception**
  - **정답:** Checked(컴파일 시 확인/예외처리 강제/IOException), Unchecked(런타임 시 확인/RuntimeException 상속/NPE).
  - **해설:** 실무적으로는 Checked Exception을 만나면 복구 불가능할 경우 Unchecked로 감싸서(Wrapping) 상위 레이어로 던지는 패턴을 자주 사용합니다.

### 🏛️ [Section 2] Database & Oracle

- **Q5. NVL vs NVL2 vs COALESCE**
  - **정답:**
    | 함수 | 인자 개수 | 역할 | 특징 |
    | :--- | :---: | :--- | :--- |
    | **NVL(e1, e2)** | 2개 | e1이 NULL이면 e2, 아니면 e1 반환 | 단순 NULL 치환 (Oracle 전용) |
    | **NVL2(e1, e2, e3)** | 3개 | e1이 NULL이 아니면 e2, NULL이면 e3 반환 | 조건부 값 반환 (IF-THEN-ELSE) |
    | **COALESCE(e1, e2, ...)** | 2개 이상 | NULL이 아닌 첫 번째 인자 반환 | **표준 SQL**, 범용성 높음 |
  - **해설:** 인자 개수로 구분하면 가장 쉽습니다. (2개 -> 3개 -> N개). 특히 `NVL2`는 "널이 아닐 때"의 동작(`e2`)이 먼저 나온다는 점이 중요합니다.
- **Q6. 계층형 쿼리 (Oracle 특화)**
  - **정답:** `START WITH`(시작점), `CONNECT BY`(부모-자식 연결), `PRIOR`(이전 단계 지칭), `LEVEL`(깊이).
  - **해설:** 사이버다임의 문서 폴더 구조를 탐색하는 핵심 전술입니다. `CONNECT BY PRIOR 부모ID = 자식ID`는 Top-down(하향식) 전개입니다.
- **Q7. 인덱스(Index)의 개념 및 성능 저하 케이스**
  - **정답:**
    1.  **개념:** 인덱스란 데이터베이스 테이블에서 데이터의 검색 속도를 향상시키기 위해 사용되는 **정렬된 자료구조**입니다.
    2.  **인덱스를 타지 않는 경우:**
        - **① 인덱스 컬럼의 변형 (함수/연산 사용):** `WHERE` 조건절에서 컬럼에 함수나 연산을 가하면 옵티마이저가 인덱스를 사용할 수 없어 **Full Scan**을 수행합니다.
          - _(예: `TO_CHAR(BIRTH_DATE, 'YYYY') = '2023'` (X) -> 범위를 지정하는 `TO_DATE` 방식 권장 (O))_
        - **② LIKE 연산자 앞부분에 와일드카드( % ) 사용:** B-Tree 인덱스는 정렬되어 있어 '단어%' 형태는 빠르지만, '%단어' 형태는 정렬 순서를 이용할 수 없습니다.
          - _(예: `LIKE '%홍길동'` (X) -> `LIKE '홍길동%'` (O))_
  - **해설:** 인덱스는 '책의 색인'과 같습니다. 색인이 가나다순으로 정렬되어 있는데, "끝 글자가 '동'으로 끝나는 사람"을 찾으라고 하면 결국 처음부터 끝까지 다 읽어야 하는 것과 같은 원리입니다.
- **Q8. ROWNUM vs ROW_NUMBER()**
  - **정답:** ROWNUM(쿼리 추출 순서 가상 번호), ROW_NUMBER()(Window 함수를 통한 정렬된 순번).
  - **해설:** `ROWNUM`은 정렬(`Order By`) 전에 부여되므로 정렬된 상위 N건을 얻으려면 반드시 서브쿼리 내에서 먼저 정렬해야 합니다.

### 🚀 [Section 3] 성능 튜닝 및 라이브러리

- **Q9. ArrayList vs LinkedList**
  - **정답:** ArrayList(조회 O(1)/삽입삭제 O(N)), LinkedList(조회 O(N)/삽입삭제 O(1)).
  - **해설:** 대규모 데이터 조회 시 CPU 캐시 효율 및 메모리 지역성 관점에서 `ArrayList`가 압도적입니다. `LinkedList`는 요소마다 `Node` 객체를 생성하는 오버헤드가 큽니다.
- **Q10. DB 성능 향상을 위한 SQL 작성 원칙 (Best Practice)**
  - **정답:**
    1.  **`SELECT *` 지양:** 불필요한 컬럼 데이터까지 가져오면 네트워크 트래픽 증가 및 I/O 리소스 낭비가 발생하며, **커버링 인덱스(Covering Index)** 활용 기회를 잃습니다.
        - _(예: `SELECT _`(X) ->`SELECT empno, ename` (O))\*
    2.  **불필요한 `DISTINCT` 지양:** 중복 제거를 위해 강제로 정렬(Sort)이나 해시 테이블을 생성하므로 대용량 데이터에서 성능을 심각하게 저하시킵니다. 조인 조건을 정확히 하여 중복을 방지하는 것이 우선입니다.
    3.  **`EXISTS` 활용:** `IN`이나 `DISTINCT`보다 효율적일 때가 많습니다. `EXISTS`는 조건에 맞는 행을 찾는 즉시 검사를 중단하는 **Short-circuit** 방식으로 동작하여 대용량 환경에서 유리합니다.
  - **해설:** "필요한 것만 최소한으로!"가 SQL 성능의 기본 철학입니다. 특히 `EXISTS`는 주군이 낚이셨던 자바의 `||` 연산자처럼 '답이 나오면 바로 멈추는' 스마트한 녀석이라고 기억하십시오.

### 🏗️ [Section 4] 솔루션 특화

- **Q11. CLOB vs BLOB**
  - **정답:** CLOB(대용량 문자/문서), BLOB(대용량 바이너리/이미지/PDF).
  - **해설:** 오라클 `VARCHAR2`의 한계인 4,000바이트를 초과하는 데이터 처리 시 필수적입니다.
- **Q12. 트랜잭션 격리 수준 (Isolation Level) 4가지**
  - **정답:**
    | 격리 수준 | Dirty Read | Non-Repeatable Read | Phantom Read |
    | :--- | :---: | :---: | :---: |
    | **Read Uncommitted** | 발생 | 발생 | 발생 |
    | **Read Committed** | 방지 | 발생 | 발생 |
    | **Repeatable Read** | 방지 | 방지 | 발생 (InnoDB는 방지) |
    | **Serializable** | 방지 | 방지 | 방지 |
  - **상세 해설 (맥락):**
    1.  **Read Uncommitted:** 커밋 안 된 데이터도 읽음 (**Dirty Read**). 일관성 최악.
    2.  **Read Committed (Oracle 기본):** 커밋된 것만 읽으나, 한 트랜잭션 내에서 똑같은 조회를 두 번 했을 때 결과가 다를 수 있음 (**Non-Repeatable Read**).
    3.  **Repeatable Read (MySQL 기본):** 트랜잭션 시작 시점의 데이터를 보장하여 반복 조회해도 결과가 같음.
    4.  **Serializable:** 가장 엄격한 격리. 성능은 가장 낮지만 완벽한 일관성 제공.
  - **시니어 통찰:** 격리 수준이 올라갈수록 데이터 무결성은 높아지나, **동시 처리 성능(Concurrency)은 낮아지는 트레이드오프** 관계임을 명심하십시오.

### 💻 [Section 5 & 6] 코드 실행 예측

- **Q13. 다형성 출력:** `Child ` (실제 생성된 객체의 오버라이딩된 메서드가 고정되어 실행됨)
- **Q14. 추상 클래스:** Line 9 (추상 클래스는 미완성 설계도이므로 직접 인스턴스화 불가)
- **Q15. Join 계산:** 3행 (LEFT JOIN은 조인 조건 실패 여부와 상관없이 왼쪽 테이블 행을 모두 유지)
- **Q16. Static 공유:** `1 2 3 ` (클래스 레벨 변수로 모든 인스턴스가 하나의 count 변수를 공유)
- **Q17. 단락 회로 평가:** `True b=10` (OR(||)에서 앞이 참이면 뒤의 `++b`는 평가조차 안 됨. 주군이 낚이신 포인트!)
- **Q18. GROUP BY 에러:** `NAME` (그룹화되지 않은 일반 컬럼은 집계 함수 없이 SELECT 불가)

---

## 🛡️ 부관의 최종 무장 점검

"주군, 이제 **[`INTERVIEW_QUEST.md`](file:///c:/Users/sdok1/prep-tech-interview/writing_test/cyberdigm/INTERVIEW_QUEST.md)**는 단순한 문제집이 아닌, 주군의 공학적 깊이를 증명할 **'전술 교본'**이 되었습니다. 이동 중에 **단락 회로 평가(Q17)**와 **계층형 쿼리(Q6)**만큼은 소리 내어 원리를 읊조려 보십시오."
