import math

def solution(fees, records):
    answer = []
    basic_time, basic_parking_fee, unit_time, unit_fee = fees
    def time_to_minute(time):
        minute_time = int(time[:2]) * 60
        minute_time += int(time[3:])
        return minute_time
    
    be_charge_parking_fee_dict = {}    
    for parking_history in records:
        time, car_number, parking_status = parking_history.split(' ')
        minute_time = time_to_minute(time)
        be_paid_fee_price = 0
        if (be_charge_parking_fee_dict.get(car_number)):
            be_charge_parking_fee_dict[car_number]['during_parking_time'] = minute_time - be_charge_parking_fee_dict[car_number]['during_parking_time']
            be_charge_parking_fee_dict[car_number]['parking_status'] = parking_status
            
            if (be_charge_parking_fee_dict[car_number]['during_parking_time'] <= basic_time):
                be_charge_parking_fee_dict[car_number]['be_paid_fee_price'] = basic_parking_fee
            else:
                be_charge_parking_fee_dict[car_number]['be_paid_fee_price'] = basic_parking_fee + math.ceil((be_charge_parking_fee_dict[car_number]['during_parking_time'] - basic_time) / unit_time) * unit_fee
        else:
            be_charge_parking_fee_dict[car_number] = {'during_parking_time': minute_time, 
                                                     'parking_status': parking_status, 
                                                      'be_paid_fee_price': 0}
    # 최종 출차 시간 및 주차요금 계산
    for car_number, value_dict in be_charge_parking_fee_dict.items():
        car_number, value_dict
        if value_dict['parking_status'] == 'IN':
            be_charge_parking_fee_dict[car_number]['during_parking_time'] = 1439 - be_charge_parking_fee_dict[car_number]['during_parking_time']
            be_charge_parking_fee_dict[car_number]['parking_status'] = 'OUT'
            if (be_charge_parking_fee_dict[car_number]['during_parking_time'] <= basic_time):
                be_charge_parking_fee_dict[car_number]['be_paid_fee_price'] = basic_parking_fee
            else:
                be_charge_parking_fee_dict[car_number]['be_paid_fee_price'] = basic_parking_fee +  math.ceil((be_charge_parking_fee_dict[car_number]['during_parking_time'] - basic_time) / unit_time) * unit_fee
    # 차량번호, 금액으로 묶기
    be_paid_parking_fee_list= []
    for car_number, value_dict in be_charge_parking_fee_dict.items():
        be_paid_parking_fee_list.append((car_number, value_dict['be_paid_fee_price']))
        
    # 차량 번호 순으로 정렬,
    be_paid_parking_fee_list.sort(key=lambda x: x[0])
    print(f'{be_paid_parking_fee_list=}')
    
    # return 만들기
    answer = [ value[1] for value in be_paid_parking_fee_list ]

    return answer


fees =[180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(f"{solution(fees, records)=}")