# slice string 2866
string_cnt, string_len = map(int ,input().split())
col_str_len = [string_cnt][0]
string_matrix = []
org_column_str_list = []
for _ in range(string_cnt):
	string_matrix.append(list(str(input())))
for i in range(string_len):
	col_str = []
	for j in range(string_cnt):
		col_str += string_matrix[j][i]
	org_column_str_list.append(''.join(col_str))

start = 0
end = col_str_len
while(start <= end):
	mid = (start + end)//2
	cur_str_set = set()
	cur_column_str_list = []
	for idx in range(string_len):
		cur_column_str_list.append(org_column_str_list[idx][mid:])
		cur_str_set.add(org_column_str_list[idx][mid:])
	if (len(cur_column_str_list) != len(cur_str_set)):
		end = mid - 1
	else:
		start = mid + 1
print(start-1)


