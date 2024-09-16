'''
2회 이상 나타나면서 떨어져 있으면서 2개 이상의 부분
각 문자 별 최대 길이와 전체 개수가 다르면 외톨이 알파벳
이전에 나왔었음을 알아야함
'''

from collections import defaultdict 
def solution(input_string):
    loner_alphabets = ''
    alpha = defaultdict(int)
    prev_alpha = ''
    for ch in input_string:
        if alpha[ch] > 0 and \
            prev_alpha != ch and \
            ch not in loner_alphabets:
            loner_alphabets += ch
        alpha[ch] += 1
        prev_alpha = ch
    result = ''.join(sorted(loner_alphabets))
    return result if result else 'N'
