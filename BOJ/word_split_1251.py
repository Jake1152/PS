word = input()
ascii_list = []
for ch in list(word):
    ascii_list.append(ord(ch))
for asc in sorted(ascii_list):
    print(chr(asc), end='')


'''
1. 문제이해
- 단어를 3부분으로 나눈다.즉 구분점은 2개
- 나눈 각 단어를 역순으로 만든다.
- 그리고 합친다.


2. 문제재정의

3. 문제해결방법

4. 검증

5. 실행

6. 회고

'''