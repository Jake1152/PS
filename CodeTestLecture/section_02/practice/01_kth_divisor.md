# 문제이해

자연수 p,q가 있을 떄, 만일 p를 q로 나누었을 떄 나머지가 0이면 q는 p의 약수이다.

자연수 N과 K가 주어졌을떄
N의 K번째 약수를 return한다
K번째 약수가 없다면 -1을 return한다

# 문제해결방법

- N,K입력 받기
- N의 약수 구하여 divisor_arr 배열에 추가
  - 약수 구하기
    1부터 자신까지를 숫자 중 나눌 수 있는 수가 약수이다.
- 배열 divisor_arr의 길이와 k비교 k가 길이보다 k -1 이하이면 divisor_arr[k-1] return
  아니라면 -1 return

# 검증

# 실행

# 회고
