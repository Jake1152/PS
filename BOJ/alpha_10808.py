from collections import defaultdict
word = input()
a_dict = { chr(i): 0 for i in range(ord('a'), ord('z')+1) }

for ch  in list(word):
    a_dict[ch] += 1

for val in a_dict.values():
    print(val, end=' ')