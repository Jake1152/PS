목표 유저수를 최소한의 비용을 들여 달성하고자 한다.

유저수를 늘릴 수 있는 여러 방법들이 주어진다.

어떤 경우들이 있을 것인가?

- 용어정리
  - 달성유저수 => T
  - 유저를 늘릴 수 있는 방법 => M
  - 유저를 늘리기 위한
    - 마케팅 비용 => C
    - 마케팅 효과 => E

1. 달성유저수가 유저를 늘릴 수 있는 모든 방법들의 각 얻을 수 있는 유저수보다 큰 경우
   => T > M_n_C (0 <= n <= 주어진 마케팅 방법의 수)

2. T < M_k_C (k는 모든 방법이 될수 있거나 일부이거나 없을 수 있다.)

- 해당 마케팅 방법을 실행 했을 때 한번에 목표 유저수를 뛰어넘을 수 있는 경우

욕심쟁이일까?
DP일까?
완전탐색일까?
혹은 가지치기가 가능한 탐색일까?

# 해결방법

## 시뮬레이션

- 모든 마케팅 방법별로 단위당 마케팅효과를 계산한다.(얻을 수 있는 유저수)
- 가장 효율적인 방법론(단위당 마케팅 효과가 가장 큰 방법)으로 욕심쟁이 문제 풀이 방법으로 처리한다.

  - 단점으로는 효율은 좋더라도 들어가는 마케팅의 최소비용이 클 수 있다. 전체적으로 보았을 때 최소비용이 아닐 수 있다.

- 단위당 마케팅효과는 최상이 아니더라도 목표를 달성하는데에는 여러 덜 효율적인 방법론을 조합하여 최소의 비용만 들이고서 목표 유저수를 달성할 수 있다.
- 어떻게 구할 것인가?
  - 완전탐색인가?
  - DP의 요소가 있는가?
    - 중복은 무엇인가?
    - 반복되는 패턴은 무엇인가?
- 비용대비효과, 효과, 비용 순서로 정렬한다.
- 비용대비 효과
- 효과를 어떻게할 것인

500명을 늘릴려고 하는데
100,200,300명을 늘릴 수 있는 기법의 조합을 쓰는 것보다
한번에 1000명을 늘릴 수 있는 기법이 가장 비용이 덜 드는 방법일 수도 있다

어떻게 덜 계산하고 결과를 낼 것인가?

근접할 수 있을것이라 생각드는 방법은
단위비용대비효과(DESC), 효과(DESC), 비용(ASC) 등의 조건으로 주어진 모든 마케팅 방법들을 정렬을 하고서

마케팅 방법들을 확인하며 한번에 목표치를 달성할 수 있는지 확인하고
한번에 할 수 있다 했을 때 드는 비용과

한번에 할 수 없는 경우들의 조합(거스름돈 내기 해결방법 적용)의 비용을 비교해서 둘중 적은 방법을 선택한다.

즉, min(one_punch, 거스름돈내기방법로)
