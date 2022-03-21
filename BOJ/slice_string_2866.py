# slice string 2866
string_cnt, string_len = map(int ,input().split())
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
end = string_len
print(f"{org_column_str_list=}")
while(start <= end):
	mid = (start + end)//2
	cur_str_set = set()
	cur_column_str_list = []
	for idx in range(string_len):
		cur_column_str_list.append(org_column_str_list[idx][mid:])
		cur_str_set.add(org_column_str_list[idx][mid:])
		print(f"{cur_column_str_list=}")
		print(f"{cur_str_set=}")
	break


