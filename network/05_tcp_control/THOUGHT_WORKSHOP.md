# 🧠 사고의 단련장 (Thought Workshop) - TCP Flow & Congestion Control

## 📈 사고 진화 기록 (Evolution Log)

### 퀘스트 06: TCP Flow & Congestion Control - "속도의 완급 조절"

#### 🛡️ 1단계: 초기 인식 (Intuition)

- "신뢰성(Reliability)을 확보했으니, 이제는 얼마나 '빨리' 그리고 '안전하게' 보낼 것인가의 싸움이다."
- "Flow Control은 수신자가 숨 가쁘지 않게 해주는 배려이고, Congestion Control은 네트워크라는 고속도로가 막히지 않게 하는 공익적 절제다."

---

#### 🏗️ [Stage 1]: 흐름 제어(Flow Control) - 수신자의 권력

##### ⚡ 사고의 균열 & 교정 (Reflection)

- **균열:** "TCP 바이트 스트림은 왜 `Next Seq Expected`를 ACK 번호로 쓸까? 그냥 받은 번호를 ACK 하면 안 되나?"
- **교정 (Senior Insight):** 이것은 **'기대 기반(Expectation-based)'** 응답의 미학입니다. 수신자가 "다음엔 n번부터 줘!"라고 명확히 지시함으로써, 송신자는 별도의 계산 없이 ACK 번호를 자신의 다음 `send_base`로 즉시 일치시킵니다. 송수신자 윈도우의 톱니바퀴를 가장 직관적으로 결합하는 공학적 선택입니다.

##### 🖼️ 사고의 시각화

![TCP Byte Stream ACK Logic](../tcp_control/TCP_byte_stream_ACKs.png)

##### 💎 사고의 진화 (Evolution)

- **[2026-03-19 - Byte Stream ACK Insight]**: "TCP의 ACK 번호(`Last+1`)는 단순한 응답이 아니라, **송신자에게 날리는 '다음 작업 지시서'**다. 이 1바이트의 차이가 송수신자 윈도우의 완벽한 동기화를 만들어낸다."
- **[2026-03-19 - Receiver's Cumulative ACK Insight]**: "누적 ACK는 수신자에게도 성역이다. Gap이 메워지기 전까지는 데이터를 상위 앱으로 올려보낼 수(Delivery) 없고, 이 정체 현상이 `rwnd`를 압박한다. 즉, **흐름 제어는 수신 버퍼라는 물리적 한계가 낳은 필연적 결과**다."

---

#### 🏗️ [Stage 2]: 기민한 복구 - Fast Retransmit

- **원리:** 타임아웃은 너무 느리다. 3-Duplicate ACKs를 통해 유실을 확신하고 즉시 재전송한다.
- **효율:** 수신자의 버퍼링(SR 전략) + 누적 ACK(GBN 전략)의 조합으로, Gap만 메우면 끝단까지 '점프'해서 ACK를 보낸다. 중복 전송이 사라지는 지점이다.

##### 🖼️ 사고의 시각화

![TCP Fast Retransmit](../tcp_control/TCP_fast_retransmit.png)
![TCP Retransmit Scenario](../tcp_control/TCP_retransmit_scenario.png)

---

## 🏆 오늘의 전승 요약 (Summary of Conquest)

- **수확:** TCP의 바이트 스트림 기반 ACK 구조와 Fast Retransmit의 효율성을 공학적으로 증명함.
- **통찰:** 흐름 제어(`rwnd`)가 단순한 숫자의 전달이 아니라, 수신자 버퍼 내의 Gap 정체 현상과 물리적으로 연결되어 있음을 꿰뚫음.
- **다음 전술:** 이제 네트워크 전체의 체증을 관리하는 **혼잡 제어(Congestion Control, `cwnd`)**의 3단계 메커니즘(Slow Start, Avoidance, Recovery)으로 진격할 준비를 마침.
