from collections import deque


def dbl_linear(n):
    lowest_num = 0
    itr = 0
    eq_one = deque([])
    eq_two = deque([])
    while True:
        if itr > n:
            return lowest_num
        eq_one.append(2 * lowest_num + 1)
        eq_two.append(3 * lowest_num + 1)
        lowest_num = min(eq_one[0], eq_two[0])
        if lowest_num == eq_one[0]:
            eq_one.popleft()
        if lowest_num == eq_two[0]:
            eq_two.popleft()
        itr += 1
