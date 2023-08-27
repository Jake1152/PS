
'''
최적화 없이 일단 진행
'''
def solution(numbers):
    answer = []
    # decimal_number = int(x)
    # full_binary_tree_node_count_list = [ 2 ** i - 1 for i in ]
    full_binary_tree_node_count_list = []
    power = 1
    _max = 10 ** 16
    full_binary_tree_node_count = 0
    while (_max > full_binary_tree_node_count):
        full_binary_tree_node_count = 2 ** power - 1
        full_binary_tree_node_count_list.append(full_binary_tree_node_count)
        power += 1
    # print(f"{full_binary_tree_node_count_list=}")
    # print(f"# {len(full_binary_tree_node_count_list)=}")

    for number in numbers:
        binary_representation = bin(number)[2:]
        print(f"{binary_representation=}")
        print(f"# {len(binary_representation)=}")
        current_binary_representation_len = len(binary_representation)
        # 같거나 작기 시작할때 알맞은 크기를 구하고서 break
        full_binary_tree_size = [current_binary_representation_len][0]
        '''
        [v] - 이진수의 길이와 알맞은 포화이진트리 크기를 찾는다
        [v] - 이진수 길이가 더 짧으면 알맞은 포화이진트리 크기만큼 0을 이진수 앞에 추가해준다.
        [] - 이진트리 생성
        [] - 이진트리에 넣으면서 확인
        '''
        for full_binary_tree_node_count in full_binary_tree_node_count_list:
            if current_binary_representation_len <= full_binary_tree_node_count:
                full_binary_tree_size = full_binary_tree_node_count
                break
        # print(f"{full_binary_tree_size=}")
        if (full_binary_tree_size > current_binary_representation_len):
            pass
        zero_list = [ "0" for _ in range(full_binary_tree_size - current_binary_representation_len)]
        binary_string = ''.join([''.join(zero_list), binary_representation])
        print(f"## {binary_string=}")
        # ''.join([''.join(zero_list), binary_representation])
        # "0101010"
        # ''.join([(''.join(zero_list)), current_binary_representation_len])
        # current_binary_string = ''.join([(''.join(zero_list)), current_binary_representation_len])
        # print(f"{current_binary_string=}")
            


    return answer

# numbers = [7,42,5]
numbers = [63, 1212323, 94]
print(f'#{solution(numbers)=}')
# [1,1,0]
'''
10 ** 15보다 작은 범위에서 찾을수있는가>
'''
# btree_node_size_list = []
# print(f"{binary_representation=}")


