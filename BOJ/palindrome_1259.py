while (True):
    n = input()
    if (n == "0"):
        break
    if (len(n) == 1):
        print("yes")
        continue
    for idx in range(len(n)//2):
        if (n[idx] != n[-idx-1]):
            print("no")
            break
    else:
        print("yes")