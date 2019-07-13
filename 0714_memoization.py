# 알고리즘스터디 시즌 2
'''
- date: 2019-07-14
- participants: @yoonjoo-pil, @cjttkfkd3941
- chapter(s): Memoization and Dynamic Programing
'''

# 8.1
def tripleStep(n):
    if n <= 2:
        return n
    if n == 3:
        return 4
    a, b, c = 1, 2, 4
    
    for i in range(4, n + 1):
        temp = a + b + c
        a, b, c = b, c, temp
    return temp

# 8.2
def gridSearch(r, c, prohibited=[]):
    from collections import deque
    nextt = deque()
    path = [None] * (r + c + 1)
    pos = (0, 0)
    idx = 0
    while (pos[0] < r or pos[1] < c):
        path[idx] = pos
        nextt.append((idx + 1, (pos[0] + 1, pos[1])))
        nextt.append((idx + 1, (pos[0], pos[1] + 1)))
        while True:
            if not nextt:
                return 'no path possible'
            idx, temp = nextt.pop()
            if temp not in prohibited and temp[0] <= r and temp[1] <= c:
                pos = temp
                print(pos)
                break
    path[-1] = pos
    return path
