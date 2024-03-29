# 문제이해
이진트리로 값을 표현 
중간에 있는 노드가 비어있을 수는 없다

어떤 수를 이진트리로 표현 
1. 이진수를 저장할 빈 문자열 생성
2. 주어진 이진트리에 더미 노드를 추가하여 포화 이진트리로 만든다. 루트노드는 그대로 유지한다.
3. 만들어진 포화 이진트리의 노드들을 가장 왼쪽 노드부터 가장 오른쪽 노드까지, 왼쪽에 있는 순서대로 살펴본다. 노드의 높이는 살펴보는 순서에 영향을 끼치지 않는다.

4. 살펴본 노드가 더미 노드라면, 문자열 뒤에 0을 추가합니다. 살펴본 노드가 더미 노드가 아니라면, 문자열 뒤에 1을 추가합니다.
5. 문자열에 저장된 이진수를 십진수로 변환합니다.

이진트리에서 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브트리의 노드들보다 오른쪽에 있으며, 자신의 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정합니다.

in-order로 순회
- 주어진 숫자를 이진수로 표현한 다음에 해당 숫자로 이진트리로 표현가능한지 아닌지를 return한다.

# 문제 재정의

- 주어진 숫자를 이진수로 표현한 다음에 
변환한 이진수를 in-order로 포화이진트리로 표현했을 때,
단말노드를 제외하고는 0이 있지 않으면 이진트리가 성립한다.

7 == 0111
42 == 010 1010

# 문제 해결방법
## way1
- 숫자를 이진수로 변환한다.
    - python이용
    - 이진트리에 맞는 길이어야하므로 
      변환한 이진수의 문자열 길이에 따라 
      포화이진트리 길이에 알맞게 더미숫자를 추가한다.
      e.g) 길이 6 => 7로 맞추어줌
        포화이진트리, 0
           2**n - 1 길이가 되어야한다.
    - 범위가 10**15 이므로 
    2**n -1 값이 10**(15+1) 보다 작은 동안 그 값들을 순서대로 배열에 넣는다.
    어떤 숫자가 주어졌을때 변환한 이진수를 포화 이진트리로 변환했을때 알맞은 길이로  이분탐색하게하는 용도이다.
- 이진수를 in-order를 기준으로 binary tree로 만든다.
    - in-order를 pre-order로 변환한다. 
    '0' -> '1'
    return 0
- binary tree 중간 노드가 dummy인지 확인하며 끝까지 비단말 노드 중에 dummy가 없으면 1, 하나라도 있으면 0을 answer list에 추가한다.
10^15 ->  10^15 -> 2진수 -> 40자리
2**1 -> 2**n 
array 1만 


[ 2**n -1, ]

[1, 3, 7, ... ,2**n -1]

<!-- ㅓ18,446,744,073,709,551,615 -->
<!-- 12,345,678,901,234,567,890 -->

## way2
- 숫자를 이진수로 변환
- 주어진 숫자를 이진트리로 변환하지 않고 확인할 수 있는 방법을 찾는다.
    - 비단말노드가 0이라면 no이다.
    - 일단 이진트리로 변환할 수 있게 더미들을 추가한다?
    그런데 더미는 항상 앞에부터 채우는가 아니면 뒤에도 채워도 되는가?
    둘 다를 채워보고 테스트 해봐야하는가?
    뒤에는 채우면 다른 숫자가 되니까 채울 수 없다.
    앞에서부터 채워야한다. 그래야 이진수 값에 변화가 없다.

# 문제 검증



# 실행



# 회고 




