# slice string 2866
string_cnt, string_len = map(int ,input().split())
string_matrix = []
column_str_list = []
for _ in range(string_cnt):
	string_matrix.append(list(str(input())))
for i in range(string_len):
	col_str = []
	for j in range(string_cnt):
		col_str += string_matrix[j][i]
	column_str_list.append(''.join(col_str))

start = 0
end = string_len

while(start <= end):
	mid = (start + end)//2
	pass

