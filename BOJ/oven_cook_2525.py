# 2525
hour, minute = map(int, input().split())
cooking_time = int(input())
add_hour = (cooking_time + minute) // 60
minute = (cooking_time + minute) % 60
hour = (add_hour + hour) % 24
print(str(hour) + ' ' +  str(minute))
