#2021 KAKAO BLIND RECRUITMENT
#신규 아이디 추천

'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')

# test1 = re.sub('(([a-zA-Z0-9])\\2{4,})', '.', test)

'''
import re

def solution(new_id):    
    new_id = new_id.lower()
    print(new_id)
    new_id = ''.join(re.compile("[0-9a-z-_.]").findall(new_id))
    print(new_id)
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)
    print(new_id)
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    print(new_id)
    if not new_id:
        return "aaa"
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    new_id = re.sub('\.$', '', new_id)
    # ^.$ remove
    
    # print(''.join(new_id))
    return new_id[:15]

# new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "123_.def"
# "...!@bat#*..y.abcdefghijklm"
print(solution(new_id))


# test = 'abbbsdfcdZZZZ11111)'
# test1 = re.sub('(([a-zA-Z0-9])\\2{4,})', '.', test)

# print(test1)
