gate_cnt = int(input())
plane_cnt = int(input())
plane = []
docking = [i for i in range(1, gate_cnt+1)]
for _ in range(plane_cnt):
    plane.append(int(input()))
print(len(plane))