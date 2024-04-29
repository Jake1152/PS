def solution():
    pass
# dp =  

'''
함수 안에서 yield 키워드를 쓰면 그 함수는 제너레이터가 된다.
- 제너레이터에 있는 값을 변경하는 방법 필요
- 제너레이터를 이용해서 dp배열 구성
'''
def gen():
    pass

test_case = int(input())
for _ in range(test_case):
    start, end = list(map(int, input().split()))

    # 상대거리로 초기화
    end = end - start
    start = 0
    
    solution(start, end)
    print(f"{start=}, {end=}")


''' ref
# generator
- https://velog.io/@jewon119/TIL30.-Python-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0Generator-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC
- https://tibetsandfox.tistory.com/28
'''