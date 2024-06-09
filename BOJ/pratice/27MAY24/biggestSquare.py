current_bsq_size = 0

n, m = list(map(int, input().split()))
area = []
for _ in range(n):
    area.append(list(map(int, input())))
print(f"{area=}")

try_bsq_size = min(n, m)
print(f"{try_bsq_size=}")

# for row in range(n):
#     for col in range(m):
#         print(area[row][col], end=' ')
#     print()

def get_try_bsq_size(x_coordinate, y_coordinate) -> int:
    area_base_length = n, 
    area_height_length = m,
    base_length = area_base_length - x_coordinate
    height_length = area_height_length - y_coordinate
    
    # 높이와 밑변 중 작은 것이 현재좌표에서 구할 수 있는 최대 정사각형의 크기이다.
    return min(base_length, height_length)
'''
현재 좌표로부터 확인할 수 있는 가장 큰 정사각형의 변의 길이(try_bsq_size)를 구한다.
try_bsq_size가 current_bsq_size보다 크면 bsq가 될 수 있는지 확인여부를 return한다.

isItGoodToGetBsqSize
'''
def isItGoodToGetBsqSize(x_coordinate, y_coordinate) -> bool:
    try_bsq_size = get_try_bsq_size(x_coordinate, y_coordinate)
    return try_bsq_size > current_bsq_size

# 꼭지점들부터 확인한다.
# 받는 파라미터는 
# 좌표와, 변의 길이
# 4방향으로 확인했을 때 1이 있는지 확인한다.
'''
일일이 확인?

'''
def check_bsq(init_x_coordinate, init_y_coordinate, side_length) -> bool: 
    for x_coordinate in range(init_x_coordinate, init_x_coordinate + side_length):
        for y_coordinate in range(init_y_coordinate, init_y_coordinate + side_length):
            if (area[x_coordinate][y_coordinate] == 0):
                return False
    return True

'''
좌표를 받고, 
시도할 bsq 사이즈를 구한다.
현재 x,y 좌표와 변의 길이를 넘겨서 check_bsq()를 호출한다.

파라메트릭 서치를 통해서 현재 좌표에서 가질 수 있는 최대 bsq 크기를 구한다.

'''
def get_bsq_size(x_coordinate, y_coordinate) -> int:
    try_bsq_size = get_try_bsq_size(x_coordinate, y_coordinate)

    begin = current_bsq_size
    end = try_bsq_size
    while (begin <= end):
        side_length = (begin + end) // 2 # side_length => mid
        
        if (check_bsq(x_coordinate, y_coordinate, side_length)):
            begin = side_length + 1
        else:
            end = side_length - 1
    return end

'''
각 좌표마다 bsq사이즈를 구한다.

'''
for x_coordinate in range(n):
    for y_coordinate in range(m):
        if isItGoodToGetBsqSize(x_coordinate, y_coordinate):
            current_bsq_size = get_bsq_size(x_coordinate, y_coordinate)
            
        # print(area[x_coordinate][y_coordinate], end=' ')
print(current_bsq_size)
