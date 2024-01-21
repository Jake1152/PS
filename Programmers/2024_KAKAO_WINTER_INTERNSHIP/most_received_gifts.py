'''
# 사람별로 다른 사람에서 선물을 준 갯수, 받은 갯수, 선물지수(준것cnt - 받은것cnt)를 기록
# 갯수가 같은 경우에 선물지수 비교
'''
from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    # 자료구조 생성 
    account_dict = {}
    for friend in friends:
        account_dict[friend] = {'gift_score': 0, 'assume': 0, 'account_book': defaultdict(int)}
        for my_friend in friends:
            if my_friend != friend:
                account_dict[friend]['account_book'][my_friend] = 0
    # 기록 누적 record
    for gift in gifts:
        sender, receiver = gift.split()
        account_dict[sender]['gift_score'] += 1
        account_dict[sender]['account_book'][receiver] += 1
        account_dict[receiver]['gift_score'] -= 1
    # 받을 선물 추정치 계산, 동률인 경우 포함
    '''
    나라는 사람과 내가 선물 준 다른 친구들과의 선물 주고 받은 갯수의 차이를 계산
    '''
    for key, value in account_dict.items():
        for my_friend_name, my_sent_cnt in value['account_book'].items():
            # 내가 받은 갯수
            my_received_cnt = account_dict[my_friend_name]['account_book'][key]
            if my_sent_cnt > my_received_cnt:
                account_dict[key]['assume'] += 1
            elif my_sent_cnt == my_received_cnt and account_dict[key]['gift_score'] > account_dict[my_friend_name]['gift_score']:
                account_dict[key]['assume'] += 1
    for _dict in account_dict.values():
        answer = max(answer, _dict['assume'])
    return answer

