def star(n, star_list):
	out = []
	print(f"\n\n{star_list=}\n\n")
	if n == 3:
		return star_list
	else:
		for i in star_list:
			out.append(i*3)
		for i in star_list:
			out.append(i+' '*len(star_list)+i)
		for i in star_list:
			out.append(i*3)
		return star(n//3, out)
n = int(input())
base_star_sqaure = ['***', '* *', '***']
result_star_square = star(n, base_star_sqaure)
for i in result_star_square:
    print(i)