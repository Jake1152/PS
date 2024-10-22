
'''
- 에라토스테네스의 체 필요
  - 전체수를 가지고 있고
  - 소수인 것의 배수들을 제거한다.

  10 ** 14 => 10,000,000,000,000
- 10 * root10
  - 32
  - 2 3 5 7 11 13 17 19 23 29 31
-   8,5,3,2, 1, 1, 1, 1, 1, 1, 1


1. B(가장 큰 값)의 제곱근을 구한다.
2. 1에서 B까지의 수 중에 소수를 구한다.
3. 소수들의 N제곱(N >= 2)을 B보다 같거나 작은 동안 구한다.
    해당 소수들의 N제곱 값이 A ~ B 범위에 해당하면 count를 증가시킨다.
'''

def is_almost_prime():
    pass

def is_prime(num: int):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def sleve_of_eratosthenes(max_range : int) -> list:
    prime_list = [ True for _ in range(0, max_range + 1)]
    idx = 2
    while (len(prime_list) > idx):
        num = prime_list[idx]
        for n in range(num * 2, max_range + 1, num):
            if n in prime_list:
                prime_list[n] = False
        # if is_prime(num):
            # 현재 값의 배수들을 제거한다.
        idx += 1
    return prime_list

def __main__():
    A, B = map(int, input().split())
    sleve_of_eratosthenes_list = sleve_of_eratosthenes(int(B ** 0.5))
    print(f"{sleve_of_eratosthenes_list=}")
    count = 0
    # 3. 
    for num in sleve_of_eratosthenes_list:
        pow = 2
        while (num ** pow <= B):
            power_num = num ** pow
            if power_num >= A and power_num <= B:
               count += 1 
            pow += 1
    return count

print(__main__())