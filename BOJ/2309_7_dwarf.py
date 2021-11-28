#2309 7 dwarf

people = []
for _ in range(9):
    people.append(int(input()))
total = sum(people)
one = 0
two = 0
for i in range(8):
    for j in range(i+1, 9):
        if total - (people[i] + people[j]) == 100:
            one = people[i]
            two = people[j]
people.remove(one)
people.remove(two)
people.sort()
for person in people:
    print(person)


# from itertools import combinations

# people = []
# for _ in range(9):
#     people.append(int(input()))
# # print(f"{people=}")
# for comb in combinations(people, 2):
#     print(f"{comb=}")
#     if (sum(comb) == 100):
#         for person in sorted(comb):
#             print(person)

# 왜 조합으로는 92퍼에서 틀리는지 모르겠다.
# 1 2 