num = input()
org = [num]
cnt = 0

while (True):
    if int(num) < 10:
        num = "0" + num
    sum = 0
    for digit in list(num):
        sum += int(digit)
    num = num[1] + str(sum)[-1]
    print(f"{num=}")
    cnt += 1
    if org[0] == num:
        break
print(cnt)