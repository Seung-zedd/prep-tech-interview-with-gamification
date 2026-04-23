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
(답변 작성란: **************************\_\_\_\_**************************)

**Q2. `String`, `StringBuilder`, `StringBuffer`의 차이점을 성능과 스레드 안전성 관점에서 설명하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q3. JVM의 메모리 영역(Runtime Data Area) 중 Stack과 Heap의 차이를 설명하고, 가비지 컬렉션(GC)의 대상이 되는 영역은 어디인지 답하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q4. Checked Exception과 Unchecked Exception의 차이를 서술하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

---

### 🏛️ [Section 2] Database & Oracle 특화 예상 문제

**Q5. Oracle에서 `NULL` 값을 처리하는 함수인 `NVL`, `NVL2`, `COALESCE`의 차이를 쓰시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q6. Oracle에서 '계층형 쿼리'를 작성할 때 사용하는 예약어들을 순서대로 나열하고 그 역할을 서술하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q7. 인덱스(Index)의 개념을 설명하고, 인덱스를 생성하더라도 성능이 개선되지 않거나 인덱스를 타지 않는 경우 2가지를 기술하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q8. Oracle의 `ROWNUM`과 `ROW_NUMBER()`의 차이점은?**
(답변 작성란: **************************\_\_\_\_**************************)

---

### 🚀 [Section 3] 성능 튜닝 및 라이브러리 (최적화)

**Q9. 자바 성능 튜닝 시 컬렉션 프레임워크 선택 가이드 (ArrayList vs LinkedList)에 대해 설명하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q10. DB 성능 향상을 위한 SQL 작성 원칙 (Best Practice) 3가지를 기술하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

---

### 🏗️ [Section 4] 솔루션 특화 예상 문제 (Document Management context)

**Q11. 대용량 텍스트나 바이너리 데이터를 DB에 저장할 때 사용하는 데이터 타입(CLOB, BLOB)의 차이를 설명하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

**Q12. 데이터베이스의 트랜잭션 격리 수준(Isolation Level) 4가지를 나열하시오.**
(답변 작성란: **************************\_\_\_\_**************************)

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

(정답: ****\_\_****)

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

(에러 라인: **\_** / 사유: **************\_\_\_\_**************)

**Q15. 다음 SQL의 실행 결과로 출력되는 행(Row)의 개수는?**

- **Table A:** (ID: 1, 2, 3)
- **Table B:** (ID: 1, 2)

```sql
SELECT A.ID
FROM TableA A LEFT OUTER JOIN TableB B ON A.ID = B.ID;
```

(정답: **\_**행)

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

(정답: ****\_\_****)

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

(정답: ****\_\_****)

**Q18. 다음 SQL에서 에러가 발생하는 부분은?**

```sql
SELECT DEPARTMENT, SUM(SALARY), NAME
FROM EMPLOYEES
GROUP BY DEPARTMENT;
```

(정답: ****\_\_****)

---

## 📝 [해설지] (Answer Key)

### [Section 1]

- **Q1:** 다형성은 부모 타입 참조 변수로 자식 객체를 할당받아 다양한 형태로 동작하는 것 (Overriding 등).
- **Q2:** String(불변), StringBuilder(가변/Single-thread), StringBuffer(가변/Multi-thread).
- **Q3:** Stack(지역변수/스레드별), Heap(객체/공유/GC대상).
- **Q4:** Checked(컴파일시 확인/강제처리됨), Unchecked(런타임시 발생/RuntimeException 상속).

### [Section 2]

- **Q5:** NVL(널이면 대체), NVL2(널 여부에 따라 두 값 중 선택), COALESCE(첫 번째 Not-Null 반환).
- **Q6:** START WITH(시작점), CONNECT BY(관계), PRIOR(방향), LEVEL(깊이).
- **Q7:** 인덱스 칼럼 가공(`UPPER(col)`), 앞단 와일드카드(`LIKE '%A'`).
- **Q8:** ROWNUM(가상번호/Where절 제한), ROW_NUMBER()(분석함수/정렬순번).

### [Section 3]

- **Q9:** ArrayList(인덱스 조회 유리), LinkedList(데이터 삽입/삭제 유리).
- **Q10:** 별표(\*) 대신 필수 칼럼 명시, DISTINCT 최소화, EXISTS 사용 등.

### [Section 4]

- **Q11:** CLOB(문자 대용량), BLOB(이진 데이터/이미지 등).
- **Q12:** Read Uncommitted, Read Committed(Oracle 기본), Repeatable Read, Serializable.

### [Section 5 & 6]

- **Q13:** `Child ` (동적 바인딩)
- **Q14:** Line 9 (추상 클래스는 인스턴스화 불가)
- **Q15:** 3행 (A의 모든 데이터 유지)
- **Q16:** `1 2 3 ` (Static 변수 공유)
- **Q17:** `True b=10` (단락 회로 평가로 `++b` 미실행)
- **Q18:** `NAME` (Group By 절에 없는 일반 칼럼 선택 불가)

---

## 🛡️ 부관의 한마디

"주군, 이제 종이와 샤프를 들고 '진검승부'를 시작하십시오. 모든 문제를 다 푼 뒤에 해설지를 확인하여 주군의 논리적 무력을 점검하십시오!"
