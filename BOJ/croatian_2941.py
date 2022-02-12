# 2941
'''
1. 알파벳 dict
2. 카운트 변수
3. 1칸씩 이동
4. 한번에 2개씩 읽음
   d이면 3개 읽기
뒤에서 2번째이면
'''

croatian_alpha = input()
alpha_len = len(croatian_alpha)
croatian_alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
for idx in range(0, alpha_len-2):
    if croatian_alpha[idx] in croatian_alpha_list:
        print(croatian_alpha[idx])
        cnt += 1
    if croatian_alpha[idx:idx+2] in croatian_alpha_list:
        print(croatian_alpha[idx:idx+2])
        cnt += 1
    if croatian_alpha[idx:idx+3] in croatian_alpha_list:
        print(croatian_alpha[idx:idx+3])
        cnt += 1
if croatian_alpha[alpha_len-2] in croatian_alpha_list:
        print(croatian_alpha[idx-1])
        cnt += 1
if croatian_alpha[alpha_len-1] in croatian_alpha_list:
        print(croatian_alpha[idx])
        cnt += 1
if croatian_alpha[alpha_len - 2:alpha_len] in croatian_alpha_list:
    print(croatian_alpha[alpha_len - 2:alpha_len])
    cnt += 1
print(cnt)