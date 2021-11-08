# 15649 N과 M(1)

# way 1 using itertools
from itertools import permutations

N, M = map(int, input().split())
num_list = [i for i in range(1,N+1)]
for permute_tuple in permutations(num_list, M):
    for num in permute_tuple:
        print(num, end=' ')
    print()

'''

# way 2 list로 permutaion 결과반환
def dfs(num_list, turns):
    ret_list = []
    pass
    

# way 1 using itertools
from itertools import permutations

N, M = map(int, input().split())
num_list = [i for i in range(1,N+1)]
for permute_tuple in permutations(num_list, M):
    for num in permute_tuple:
        print(num, end=' ')
    print()

----
# way3 yield로 반환, 하지만 낱개로 반환되면서 끝까지 잘될지 모르겠다. 메소드 중간에 끊기는 것은 아닐지
def dfs(num_list, turns):
    

    pass    
    yield

'''