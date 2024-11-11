'''
만약 갯수가 동일하다면? abcde, fghij
둘은 동형이며 매핑이 된다 
a b c d e
1 1 1 1 1

f g h i j
1 1 1 1 1 

매핑이 된다는 특징이 있다
다른 값으로 바꾸었을때 치환이 된다.

사과잼, 딸기잼 만들기
사과 300g + 설탕 50g
딸기 300g + 설탕 50g 
서로 동형
하지만 양 뿐만 아니라 순서까지 변환했을 때 같아야한다.

"bbbaaaba" // a: 4, b: 3
"aaabbbba" // a: 3, b: 4
이 둘은 a,b를 바꾸었을 때, 용량은 같지만 순서가 다르다
치환이 안되므로 isomorphic이 아니다.

순서에 맞게 변환하려면 같은 개수에 있는 알파벳들을 다시 비교해봐야한다.

값의 차이로 볼 수 있는가?
가장 작은 알파벳 기준으로 값을 빼면 되는가?
특정 값으로 초기화한 뒤에 값이 같아지는지 보면 될 것인가?

aaabbba 0001110
bbbbaaa 1111000
'''
# a[26] = 0
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alpha_dict = {}
        # for in enumerate(t)
        for ch_s, ch_t in zip(s, t):
            if alpha_dict.get(ch_s) == None and ch_t not in alpha_dict.values():
                alpha_dict[ch_s] = ch_t
            elif alpha_dict.get(ch_s) == None or alpha_dict[ch_s] != ch_t:
                return False
        result = ""
        for ch_s in s:
            result += alpha_dict[ch_s]
        return result == t