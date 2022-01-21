# #z_1074

#z_1074
g_prev_order = 0
n, r, c = map(int, input().split())
def visit_zigzag(x, y, side):
    global g_prev_order
    if (x == r and y == c):
        print(g_prev_order)
        return
    if (side == 1):
        g_prev_order += 1
        return 
    visit_zigzag(x, y, side//2)
    visit_zigzag(x, y+side//2, side//2)
    visit_zigzag(x+side//2, y, side//2)
    visit_zigzag(x+side//2, y+side//2, side//2)

visit_zigzag(0, 0, 2**n)

# g_prev_order = 0
# n, r, c = map(int, input().split())
# square = [ [0 for _ in range(2 ** (n))] for _ in range(2 ** (n))]
# def visit_zigzag(x, y, side):
#     global g_prev_order
#     if (x >= r and y >= c and square[r][c] != 0):
#         return 
#     if (side == 1):
#         square[x][y] = g_prev_order
#         g_prev_order += 1
#         return 
#     visit_zigzag(x, y, side//2)
#     visit_zigzag(x, y+side//2, side//2)
#     visit_zigzag(x+side//2, y, side//2)
#     visit_zigzag(x+side//2, y+side//2, side//2)

# visit_zigzag(0, 0, 2**n)
# print(square[r][c])