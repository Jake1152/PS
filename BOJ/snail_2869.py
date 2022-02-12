#snail 2869

a, b, v = map(int, input().split())
v = v - a + (a-b)
if v % (a-b) == 0:
	days = (v // (a-b))
else:
	days = (v // (a-b)) + 1	

print(days)
