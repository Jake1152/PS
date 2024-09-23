'''
멘델 완두콩 
자가 수분 실험 결과 정리 
전부 기록하는 것 대신, 완두콩의 세대와 해당 세대에서 몇 번쨰 개체인지를 알면 형질을 바로 계산하는 프로그램을 만듦
'''

'''
재귀적으로 반복됨
1:2:1의 비율
2의 비율안에 들어간다면

4등분 했을 때, 몇 분기에 해당하는지 확인
4개가 남을때까지 진행
4, 26

4 ** 3 =>  64,
16,32,
17 ~ 32
4 ** 2
26 - 16(앞에 있는 분기 수 만큼 뺄셈)
=> 10
1/4, 2/4, 3/4, 4/4 분기 중 어디에 해당하는가?
3/4 분기라면 2개 분기만큼 빼기
'''

green_pea_type = ["RR", "Rr", "Rr", "rr"]

def find_green_pea_type(generation, nth_order):
    if generation <= 2:
        return green_pea_type[nth_order - 1]
    quarter_size = 4 ** (generation - 2)
    quarter_count = 1
    while (nth_order > quarter_size):
        nth_order -= quarter_size
        quarter_count += 1
    # print(f"{quarter_count=}")
    if (quarter_count == 1):
        return "RR"
    elif (quarter_count == 4):
        return "rr"
    return find_green_pea_type(generation - 1, nth_order)

def solution(queries):
    answer = []
    
    for query in queries:
        generation, nth_order = query
        answer.append(find_green_pea_type(generation, nth_order))
    return answer

# 4 ** (generation - 1)
# [1, 1]
# 4 ** (1 - 1) => 4 ** 0 => 1

# [2, 1~4]
# 4 ** (2 - 1) => 4 ** 1 => 4, 1:2:1

# [3, 1~16]
# 4 ** (3 - 1) => 4 ** 2 => 16, 1:2:1 => 4,8,4

# [4, 1~64]
# 4 ** (4 - 1) => 4 ** 3 => 64, 1:2:1 => 16,32,16

# [4, 1~256]
# 4 ** (4 - 1) => 4 ** 4 => 256, 1:2:1 => 64,128,64  / 1~64, 65~192, 

