input_str = input()
str_len = len(input_str)
idx = 0
while (str_len//2 > idx):
    if (input_str[idx] != input_str[(idx * -1) - 1]):
        print(0)
        break ;
    idx += 1
else:
    print(1)
    