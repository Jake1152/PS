# to_be_hotel_member_counts, 

def 거스름돈내기방법(목표유저수, 마케팅방법들):
    마케팅총비용 = 0
    현재남은_목표유저수 = [목표유저수][0]

    idx = 0
    while (현재남은_목표유저수 > 0):
        # for 마케팅방법 in 마케팅방법들:
        마케팅방법 = 마케팅방법들[idx]
        print(f"{마케팅방법=}")
        _, 마케팅비용, 얻을수있는유저수 = 마케팅방법

        현재마케팅기법최대사용가능횟수 = 현재남은_목표유저수 // 얻을수있는유저수
        현재남은_목표유저수 = 현재남은_목표유저수 % 얻을수있는유저수
        마케팅총비용 += 마케팅비용 * 현재마케팅기법최대사용가능횟수
        idx += 1
    
    return 마케팅총비용

def 한번에내기(목표유저수, 마케팅방법들):
    if (마케팅방법들 == []):
        return 9999999
    return 9999999

def main():
    목표유저수, 마케팅방법의갯수 = map(int, input().split())

    '''
    적어도 C명의 고객을 얻기 위해 투자해야하는 최소금액

    # 정렬기준
    - 단위 비용당 효과가 큰 것 
    - 가급적 비용이 적은 것
    '''
    마케팅방법들 = []
    for _ in range(마케팅방법의갯수):
        마케팅비용, 얻을수있는유저수 = list(map(int, input().split()))
        얻을수있는유저수_당_비용 = round(얻을수있는유저수 / float(마케팅비용) , 2)

        마케팅방법들.append((얻을수있는유저수_당_비용, 마케팅비용, 얻을수있는유저수))
        # print(f"{얻을수있는유저수_당_비용=}")

    print(f"{마케팅방법들=}")

    단위비용기준으로_정렬된_마케팅방법들 = sorted(마케팅방법들, key=lambda x: (-x[0], x[1], -x[2]))
    print(f"{단위비용기준으로_정렬된_마케팅방법들=}")

    효과기준으로_정렬된_마케팅방법들 = sorted(마케팅방법들, key=lambda x: (-x[2], -x[0], x[1]))
    print(f"{효과기준으로_정렬된_마케팅방법들=}")

    # 한번에_목표치_달성가능한_마케팅방법들 = [ 마케팅방법 if 마케팅방법[2] > 목표유저수 for 마케팅방법 in 효과기준으로_정렬된_마케팅방법들 ]
    한번에_목표치_달성가능한_마케팅방법들 = list(filter(lambda 마케팅방법: 마케팅방법[2] >= 목표유저수, 효과기준으로_정렬된_마케팅방법들))
    print(f"{한번에_목표치_달성가능한_마케팅방법들=}")

    단위비용기준으로_정렬된_한번에_목표치_달성_가능한_마케팅방법 = sorted(한번에_목표치_달성가능한_마케팅방법들, key=lambda x: (-x[0], x[1], -x[2]))
    print(f"{단위비용기준으로_정렬된_한번에_목표치_달성_가능한_마케팅방법=}")


    조합으로_목표치_달성가능한_마케팅방법들 = list(filter(lambda 마케팅방법: 마케팅방법[2] < 목표유저수, 효과기준으로_정렬된_마케팅방법들))
    print(f"{한번에_목표치_달성가능한_마케팅방법들=}")

    단위비용기준으로_정렬된_조합으로_목표치_달성가능한_마케팅방법들  = sorted(조합으로_목표치_달성가능한_마케팅방법들, key=lambda x: (-x[0], x[1], -x[2]))
    print(f"{단위비용기준으로_정렬된_조합으로_목표치_달성가능한_마케팅방법들 =}")

    # 효과및단위비용기준_정렬된_마케팅방법들 = sorted(효과기준으로_정렬된_마케팅방법들, key=lambda x: (-x[2], -x[0], x[1]))

    '''
    효과기준으로 내림차순 정렬을 한 뒤 
    한번에 할 수 있는 경우들 중에 가장 효율적인 경우를 찾는다. 
    '''
    # 마케팅방법 정렬
    # 마케팅방법들.sort()

    # start_idx = 0
    한번에낼때의최소비용 = 한번에내기(목표유저수, 단위비용기준으로_정렬된_한번에_목표치_달성_가능한_마케팅방법)
    거스름돈내기방법쓸때의최소비용 = 거스름돈내기방법(목표유저수, 단위비용기준으로_정렬된_조합으로_목표치_달성가능한_마케팅방법들)
    목표를달성하는데드는최소비용 = min(한번에낼때의최소비용, 거스름돈내기방법쓸때의최소비용)
    print(목표를달성하는데드는최소비용)

if __name__ == "__main__":
    main()