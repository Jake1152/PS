def find_posi(num, keypad):
	for row, row_ele in enumerate(keypad):
		for col, col_ele in enumerate(row_ele):
			if num == col_ele:
				return [row, col]

def solution(numbers, hand):
	answer = ''
	keypad = [ [1,2,3], [4,5,6], [7,8,9], ['*',0,'#'] ]
	prev_left = [3, 0]
	prev_right = [3, 2]
	for num in numbers:
		if num in [1,4,7]:
			pass
			answer += 'L'
			prev_left = find_posi(num, keypad)
		elif num in [3,6,9]:
			answer += 'R'
			prev_right = find_posi(num, keypad)
		else:
			middle_line = find_posi(num, keypad)
			# print(f"{num=}")
			# print(f"{middle_line=}")
			
			left_distance = abs(middle_line[0]-prev_left[0]) + abs(middle_line[1]-prev_left[1])
			right_distance = abs(middle_line[0]-prev_right[0]) + abs(middle_line[1]-prev_right[1])
			# print(f"{left_distance=}")
			# print(f"{right_distance=}")
			if left_distance < right_distance or (left_distance == right_distance and hand == "left"):
				answer += 'L'
				prev_left = middle_line
			elif left_distance > right_distance or (left_distance == right_distance and hand == "right"):
				answer += 'R'
				prev_right = middle_line
	return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
'''
numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"
"LRLLLRLLRRL"
'''