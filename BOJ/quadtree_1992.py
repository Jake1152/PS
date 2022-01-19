# quadtree 1992
result = ""
square_side = int(input())
square = []
for _ in range(square_side):
    square.append(list(map(int, list(input()))))

# check area
def check_sqaure(x, y, side):
    global result
    standard_num = square[x][y]
    for i in range(x, x+side):
        for j in range(y, y+side):
            if (standard_num != square[i][j]):
                return (False)
    result += str(standard_num)
    return (True)


def quadtree(x, y, side):
    global result    
    if (check_sqaure(x, y, side)):
        return
    else:
        # 4 등분
        result += '('
        quadtree(x, y, side//2)
        quadtree(x, y+side//2, side//2)
        quadtree(x+side//2, y, side//2)        
        quadtree(x+side//2, y+side//2, side//2)
    result += ')'

quadtree(0, 0, square_side)
print(result)
