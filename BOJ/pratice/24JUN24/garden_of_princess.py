flower_type_count = int(input())

month_day = {0: 0, 1: 31, 3: 31, 5: 31, 7: 31, 8:31, 10: 31, 12:31, 2:28, 4: 30, 6: 30, 9: 30, 11: 30}
print(f"{month_day=}")
PRINCESS_START_MONTH = 3
PRINCESS_END_MONTH = 12
princess_start_day = sum([month_day[month] for month in range(PRINCESS_START_MONTH)]) + 1
princess_end_day = sum([month_day[month] for month in range(PRINCESS_END_MONTH)]) + 1
print(f"{princess_start_day=}")
print(f"{princess_end_day=}")
# 3  => 60
def to_day_type_date(bloom_month, bloon_day, fall_month, fall_day):
    start_day = 0 
    for month in range(bloom_month):
        start_day += month_day[month]
    start_day += bloon_day


    end_day = 0
    for month in range(fall_month):
        end_day += month_day[month]
    end_day += fall_day

    if (start_day < princess_start_day):
        start_day = princess_start_day

    if (end_day > princess_end_day):
        end_day = princess_end_day

    if (end_day <= start_day):
        return []
    return {"start_day" : start_day, "end_day" : end_day, "period": end_day - start_day}

flower_info_list = []
for _ in range(flower_type_count):
    bloom_month, bloon_day, fall_month, fall_day = map(int, input().split())
    flower_info = to_day_type_date(bloom_month, bloon_day, fall_month, fall_day)
    # print(f"{flower_info=}")
    if (flower_info):
        flower_info_list.append(flower_info)

# print(f"{flower_info_list=}")
flower_info_list.sort(key=lambda x:(x["start_day"], -x["period"]))
print(f"\n# After sort: \n{flower_info_list=}")
'''
- 시작 기간이 빠른 것 중 가장 오래 피어있는 꽃을 고른다.
- 다음 꽃은 이전에 고른 꽃이 지는 날짜(end_day)를 기준으로 start_day가 가장 가까운 날로 고른다.
'''

# def bin_search(flower_info, target):
#     # mid 
#     pass
'''
prev_start_day ~ prev_end_day 기간동안,
prev_end_day 날짜로부터 가장 시작일자가 가까운날부터 찾으며,
종료일자가 가장 멀리 있는 날을 찾는다.
n log n 까지가 한계이다.

- 이전에 선택한 꽃이 또 선택되고 && end_day가 princess_end_day보다 작다면 정원에 꽃이 없는 공백기간이 생기므로 return 0을 한다.
- start_day < prev_end_day && start_day > prev_start_day

부분 범위를 돌기는 하지만 n**2에 가까울 수 있디
'''
# def pick_flower(prev_sta):
prev_start_day = 0
start_position = 0
prev_end_day = [princess_start_day][0]
# end_position = len(flower_info_list)
chosen_flower_count = 0
for flower_info in flower_info_list:
    max_period_idx = start_position 
    max_period = flower_info_list[start_position]["period"]
    print(f'{prev_start_day=}')
    print(f'{prev_end_day=}')
    for idx, flower_info in enumerate(flower_info_list[start_position + 1:]):
        start_day = flower_info["start_day"]
        end_day = flower_info["end_day"]
        flower_period = flower_info["period"]
        if (start_day > prev_end_day):
            chosen_flower_count += 1
            prev_start_day = flower_info_list[max_period_idx]["start_day"]
            start_position = max_period_idx + 1
            prev_end_day = flower_info_list[max_period_idx]["end_day"]
            break 
        if (max_period < flower_period):
            max_period = flower_period
            max_period_idx = idx
    # end_position = len(flower_info_list) - 1

print(f"{chosen_flower_count=}")