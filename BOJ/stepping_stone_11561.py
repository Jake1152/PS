#stepping stone 11561
import sys
input = sys.stdin.readline

test_cnt = int(input())
for _ in range(test_cnt):
    begin = 1
    end = int(input())
    target = [end][0]
    # print(f"{target=}")
    while(begin <= end):
        mid = (begin + end)//2
        summation_val = ((mid + 1) * mid) // 2
        if summation_val == target:
            end = mid
            break
        elif summation_val > target:
            end = mid - 1
        else:
            begin = mid + 1
    print(end)
