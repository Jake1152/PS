# 15829
n = int(input())
r = 31
m = 1234567891
sum = 0
alpha_dict = {chr(alpha): alpha-96 for alpha in range(ord('a'), ord('z')+1)}
input_str = input()
for i, input_char in enumerate(list(input_str)):
     sum += alpha_dict[input_char]*(r**i)        
print(sum % m)