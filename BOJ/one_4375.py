while (True):
    try:
        n = int(input())
        digits = 1
        one_str = "1"
        while (True):
            if (int(one_str) % n == 0):
                print(digits)
                break
            digits += 1
            one_str += "1"
    except:
        break
