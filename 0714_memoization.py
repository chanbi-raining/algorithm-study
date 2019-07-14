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
                return -1
            idx, temp = nextt.pop()
            if temp not in prohibited and temp[0] <= r and temp[1] <= c:
                pos = temp
                break
    path[-1] = pos
    return path

# 8.3
def magicidx(lst, dup=False):
    N = len(lst)
    idx = 0
    if idx[-1] < 0: return False
    while idx < N:
        if lst[idx] == idx:
            return idx
        elif lst[idx] < idx:
            idx += 1
        else:
            if lst[idx] > N - 1: return False 
            idx = lst[idx] + 1 if not dup else lst[idx]
    return False

# 8.4
def partial(lst):
    N = len(lst) 
    answer = []
    if not lst: return [{}]
    for i in range(2 ** N):
        answer.append(format(i, '0' + str(N) + 'b'))
    for idx, j in enumerate(answer):
        answer[idx] = set(map(lambda x: lst[x] if j[x] == '1' else None, range(N)))
        answer[idx] = set(filter(lambda x: x != None, answer[idx]))
    return answer

# 8.5
def rec_mul(a, b):
    minn, maxx = min(a, b), max(a, b)
    mul = format(minn, 'b')
    answer = 0
    init = True
    while mul:
        if init:
            temp = maxx
            init = False
        else:
            temp += temp
        if mul[-1] == '1':
            answer += temp
        mul = mul[:-1]
    return answer

