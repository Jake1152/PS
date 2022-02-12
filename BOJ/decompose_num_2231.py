# decompose sum 2231

num = int(input())
constructor_num = 1
while (constructor_num <= num):
    decompose_sum = 0
    decompose_sum += constructor_num
    for digit_num in list(str(constructor_num)):
        decompose_sum += int(digit_num)
    if decompose_sum == num:
        print(constructor_num)
        break
    constructor_num += 1
else:
    print(0)

'''
2 0 1
4 0 2
6 0 3
8 0 4
29 0 19
38 0 28
40 0 29
47 0 37
49 0 38
51 0 39
56 0 46
58 0 47
60 0 48
62 0 49
65 0 55
67 0 56
69 0 57
71 0 58
73 0 59
74 0 64
76 0 65
78 0 66
80 0 67
82 0 68
83 0 73
84 0 69
85 0 74
87 0 75
89 0 76
91 0 77
92 0 82
93 0 78
94 0 83
95 0 79
96 0 84
98 0 85
'''