from collections import deque

def solution(queue1, queue2):
    answer = 0
    dequeue1 = deque(queue1)
    dequeue2 = deque(queue2)
    q1_sum = sum(dequeue1)
    q2_sum = sum(dequeue2)
    q_size = len(dequeue1) + len(dequeue2)
    if ((q1_sum + q2_sum) % 2) == 1:
        return -1
    while (True):
        if q_size * 3 <= answer:
            return (-1)
        if (q1_sum == q2_sum):
            break
        elif (q1_sum == 0 or \
            q2_sum == 0):
            return (-1)
        elif (q1_sum > q2_sum):
            element = dequeue1.popleft()
            dequeue2.append(element)
            q1_sum -= element
            q2_sum += element
        else:
            element = dequeue2.popleft()
            dequeue1.append(element)
            q1_sum += element
            q2_sum -= element
        answer += 1
    return answer
