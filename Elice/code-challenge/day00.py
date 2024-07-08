from itertools import permutations 

input_value = input()
today_solved_count_list = list(input_value)
permutation_result = permutations(today_solved_count_list, len(today_solved_count_list))

int_permutations = list(set(map(lambda x: int(''.join(x)), permutation_result)))

permutations_sorted = sorted(int_permutations)

begin = 0
end = len(permutations_sorted)
target = int(input_value)
while (begin <= end):
    mid = (begin + end) // 2
    if (target <= permutations_sorted[mid]):
        end = mid - 1
    else: # target > 
        begin = mid + 1

print(permutations_sorted[begin+1])

