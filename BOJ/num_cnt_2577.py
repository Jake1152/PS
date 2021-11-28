num_dict = { i: 0 for i in range(10)}
A = int(input())
B = int(input())
C = int(input())

for digit in map(int, list(str(A * B * C))):
    num_dict[digit] += 1
for val in num_dict.values():
    print(val)