sausage_count, people_count = list(map(int, input().split()))

slice_count = 0
'''
사람수로 소시지 갯수를 나누었을 때, 나누어 떨어지면 소시지를 스케일링하지 않는다.
약수인지 여부에 따라 달라진다.
'''
# if (sausage_count > people_count):
#     pass
sausage_count %= people_count 
print(f"{sausage_count=}")
if (sausage_count % people_count != 0):
    # 약수일 때
    # if (sausage_count % people_count == 0\
    #     or people_count % sausage_count == 0):
        sausage_count_scaled = sausage_count * 100
        ratio = sausage_count_scaled // people_count
        eqaul_parts_count = 100 // ratio
        slice_count = eqaul_parts_count * sausage_count - 1 - (sausage_count - 1)
    #약수가 아닐 때 
    # else:
    #     sausage_count_scaled = sausage_count * 100
    #     ratio = sausage_count_scaled // people_count
    #     eqaul_parts_count = 100 // ratio
    #     slice_count = eqaul_parts_count * sausage_count - 1 - (sausage_count - 1)

print(slice_count)
