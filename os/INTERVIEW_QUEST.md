# 📜 기술 면접 병법서: Operating System (Quest Index)

본 섹션은 OS 전역의 퀘스트 현황을 조망하는 중앙 사령부입니다.

---

## �️ OS 정복 여정 (Strategic Roadmap)

### 🟢 Phase 1: 존재의 증명 (Foundation) - [완료 🏆]

- [x] **[00_process_and_thread](./00_process_and_thread/THOUGHT_WORKSHOP.md)**: 프로세스 vs 스레드 (격리와 공유) **[Rank S]**

### 🟡 Phase 2: 공간의 지배 (Memory Architecture) - [교전 중 ⚔️]

- [x] **[01_virtual_memory](./01_virtual_memory/THOUGHT_WORKSHOP.md)**: 가상 메모리, MMU, 페이징 (정량적 정복)
- [ ] **페이지 교체 알고리즘 (Page Replacement Algorithm)**: 비정한 희생양의 선택 (내일의 목표)
- [ ] **쓰레싱(Thrashing) & 워킹셋(Working Set)**: 시스템 마비 방어 전술

### 🔴 Phase 3: 갈등의 중재 (Synchronization) - [정찰 대기 🔐]

- [ ] **임계 영역(Critical Section)**: 데이터 무결성을 위한 성벽
- [ ] **뮤텍스 vs 세마포어 (Mutex & Semaphore)**: 질서의 도구 (화장실 비유)
- [ ] **데드락 (Deadlock)**: 4대 조건과 회피(Avoidance) 논리

### ⚙️ Phase 4: 시스템의 통찰 (Advanced System)

- [ ] **CPU 스케줄러 (Scheduling)**: FCFS부터 다단계 피드백 큐까지
- [ ] **시스템 콜 & 인터럽트 (System Call & Interrupt)**: OS와 하드웨어의 대화법

---

## 📅 수련 브리핑 (Daily Briefing)

현재 **가상 메모리(Virtual Memory)** 요새의 구조적 이해를 마치고, 내일 **페이지 교체 알고리즘**이라는 관리 전략의 정수를 정복할 예정입니다.
