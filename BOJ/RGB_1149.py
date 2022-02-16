#RGB 1149
house_cnt = int(input())
paint_cost = []
# 집별로 페인트 색칠 비용 추가
for _ in range(house_cnt):
	paint_cost.append(list(map(int, input().split())))

for i in range(1, house_cnt):
    paint_cost[i][0] = min(paint_cost[i - 1][1], paint_cost[i - 1][2]) + paint_cost[i][0]
    paint_cost[i][1] = min(paint_cost[i - 1][0], paint_cost[i - 1][2]) + paint_cost[i][1]
    paint_cost[i][2] = min(paint_cost[i - 1][0], paint_cost[i - 1][1]) + paint_cost[i][2]
print(min(paint_cost[house_cnt - 1][0], paint_cost[house_cnt - 1][1], paint_cost[house_cnt - 1][2]))