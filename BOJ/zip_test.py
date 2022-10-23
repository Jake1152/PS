#zip_test

a_list = [1,2,3]
b_list = ['a', 'b', 'c', 'd']

for val1, val2 in zip(a_list, b_list):
    print(f"{val1=}")
    print(f"{val2=}")