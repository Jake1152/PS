alpha_list = [ -1 for _ in range(ord('a'), ord('z'))]
for idx, ch in enumerate(list(input())):
	al_ord = ord(ch) - 97
	if alpha_list[al_ord] == -1:
		alpha_list[al_ord] = idx

for ch in alpha_list:
	print(ch, end=' ')