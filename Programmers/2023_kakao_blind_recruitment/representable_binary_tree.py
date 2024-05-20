def solution(numbers):
    answer = []

    def check_nonterminal_node(binary_number, start, end, parent):
        parent_idx = (start + end) // 2
        if end - start == 1:
            if parent == '0' and binary_number[parent_idx] == '1':
                return False
            return  binary_number[parent_idx]

        if (binary_number[parent_idx] == '1'):
            if parent == '0':
                return False
            return check_nonterminal_node(binary_number, start, parent_idx, binary_number[parent_idx]) and \
                    check_nonterminal_node(binary_number, parent_idx + 1, end, binary_number[parent_idx])
        elif (binary_number[parent_idx] == '0'):
            return check_nonterminal_node(binary_number, start, parent_idx, binary_number[parent_idx]) and \
                    check_nonterminal_node(binary_number, parent_idx + 1, end, binary_number[parent_idx]) 
        
    for number in numbers:
        binary = bin(number)
        binary = binary[2:]
        cur_binary_number_digit = len(binary)
        binary_tree_height = 0 
        while (cur_binary_number_digit):
            cur_binary_number_digit = cur_binary_number_digit // 2
            binary_tree_height += 1
        complement_digit = (2 ** (binary_tree_height) - 1) - len(binary)
        
        while (complement_digit):
            binary = "0" + binary
            complement_digit -= 1
        is_possible_tree = check_nonterminal_node(binary, 0, len(binary), '1')
        
        if is_possible_tree:
            answer.append(1)
        else:
            answer.append(0)
    return answer

