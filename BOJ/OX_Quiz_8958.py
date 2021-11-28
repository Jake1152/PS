n = int(input())

for _ in range(n):
    sum = 0
    prev = 1
    for option in list(input()):
        if option == 'O':
            sum += prev
            prev += 1
        else:
            prev = 1
    print(sum)