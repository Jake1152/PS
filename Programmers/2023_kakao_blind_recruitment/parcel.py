def solution(cap, n, deliveries, pickups):
    parcel_accumulated_distance = 0
    # 맨 끝에 있는 배송지부터 혹시나 배송, 수거할 것이 있는지 확인해서 없다면 제거한다. (중간에 비어있는 곳은 지우지 않는다.)
    be_removed_parcel_spot_cnt = 0
    for idx in range(n-1, -1, -1):
        if ((deliveries[idx] == 0) and (pickups[idx] == 0)):
            be_removed_parcel_spot_cnt += 1
        else:
            break
    n -= be_removed_parcel_spot_cnt
    delivery_list = [ idx for idx, home in enumerate(deliveries) if home]
    pickup_list = [ idx for idx, home in enumerate(pickups) if home]
    delivery_list_end_idx = len(delivery_list)
    pickup_list_end_idx = len(pickup_list)
    while (delivery_list_end_idx > 0 or pickup_list_end_idx > 0):
        print(f"{delivery_list_end_idx=}")
        print(f"{pickup_list_end_idx=}")
        parcel_capacity_dict = {'total_cap': cap, 'delivery': cap , 'pickup': cap}
        # 가장 먼 곳부터 배달
        parcel_accumulated_distance += n
        print("# delivery")
        for idx in delivery_list[delivery_list_end_idx::-1]:
            print(f"{idx=}")
            if (parcel_capacity_dict['delivery'] == 0):
                break
            if (deliveries[idx] and parcel_capacity_dict['delivery']):
                be_deliveried_cnt = min(parcel_capacity_dict['delivery'], deliveries[idx])
                parcel_capacity_dict['delivery'] -= be_deliveried_cnt
                deliveries[idx] -= be_deliveried_cnt
        # 수거
        print("# pickup")
        parcel_accumulated_distance += n
        for idx in pickup_list[pickup_list_end_idx::-1]:
            print(f"{idx=}")
            if (parcel_capacity_dict['pickup'] == 0):
                break
            if (pickups[idx] and (parcel_capacity_dict['pickup'])):
                be_pickuped_cnt = min(parcel_capacity_dict['pickup'], pickups[idx])
                parcel_capacity_dict['pickup'] -= be_pickuped_cnt
                pickups[idx] -= be_pickuped_cnt
        # 더 이상 배달, 수거할 것 없는 곳 제거, 
        be_removed_parcel_spot_cnt = 0
        for idx in delivery_list[delivery_list_end_idx:0:-1]:
            if (deliveries[idx] == 0):
                be_removed_parcel_spot_cnt += 1
            else:
                break
        delivery_list_end_idx -= be_removed_parcel_spot_cnt
        be_removed_parcel_spot_cnt = 0
        for idx in pickup_list[pickup_list_end_idx:0:-1]:
            print(f"#{idx=}")
            print(f"#{pickup_list_end_idx=}")
            # print(f"{pickup_list[idx]=}")
            if (pickups[idx] == 0):
                be_removed_parcel_spot_cnt += 1
            else:
                break
        print(f"{be_removed_parcel_spot_cnt=}")
        pickup_list_end_idx -= be_removed_parcel_spot_cnt
        # delivery_list_end_idx = max(delivery_list_end_idx, 0)
        # pickup_list_end_idx = max(pickup_list_end_idx, 0)
        print(f"{delivery_list_end_idx=}")
        print(f"{pickup_list_end_idx=}")
        n = max(delivery_list[delivery_list_end_idx], pickup_list[pickup_list_end_idx])
        print(f"{n=}")
    print(f"{delivery_list_end_idx=}")
    print(f"{pickup_list_end_idx=}")
    return parcel_accumulated_distance

cap, n, deliveries, pickups = 4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]
# cap, n, deliveries, pickups = 2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]
print(f"{solution(cap, n, deliveries, pickups)=}")



