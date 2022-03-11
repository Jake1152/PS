# print_star_11 2448

def star(n, star_list):
    out = []
    if n == 3:
        return star_list
    for star_row in star_list:
        out.append(star_row)


n = int(input())
base_star_sqaure = [['  ', '*' ,'  '], [' * * '], '*****']
result_star_square = star(n, base_star_sqaure)
for i in result_star_square:
    print(i)
'''

k=0
k=1일때가 다르다
점화식을 찾아야한다.
print start 10과는 또 다르다.
  *  
 * * 
*****
이 모습이 가장 기본이 되는 사이즈이다
k가 1일떄는 달라진다.
삼각형 3개 역삼각형 1개로 구성된다.
정확히는 4개다 같은 크기의 정삼각형이다.
삼각형만 찍는게 아니라 삼각형 밖에 빈공간도 표현해야한다.

'''