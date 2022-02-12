n = int(input())

sequence = []
stack = []
clone_sequence = []
answers = []
for _ in range(n):
    sequence.append(int(input()))
index = 0
num = 1
while (num <= n):
    if stack and stack[-1] == sequence[index]:
        clone_sequence.append(stack.pop())
        answers.append("-")
        index += 1
    else:
        stack.append(num)
        num += 1
        answers.append("+")
while stack:
    clone_sequence.append(stack.pop())
    answers.append("-")

if clone_sequence == sequence:
    for stack_command in answers:
        print(stack_command)
else:
    print("NO")