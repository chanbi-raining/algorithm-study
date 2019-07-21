# 알고리즘스터디 시즌 2
'''
- date: 2019-07-14, 2019-07-21
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


# 8.7
def permute(string):
    N = len(string)
    if N <= 1:
        return {string}
    if N == 2:
        return {string, string[1] + string[0]}
    
    answer = set()
    for i in permute(string[1:]):
        for k in range(len(i) + 1):
            answer.add(i[0:k] + string[0] + i[k:])
    return answer


# 8.9
def parentheses(N):
    if N == 0: return set()
    if N == 1: return {'()'}
    answer, temp = set(), set()
    for i in parentheses(N - 1):
        answer.add('()' + i)
        answer.add('(' + i + ')')
        answer.add(i + '()')
    return answer


# 8.11
def cntcoin(n):
    coins = [0, 1]
    N = len(coins)
    if n <= 1:
        return coins[n]
    while n >= N:
        temp = 0
        temp += 1 if N % 5 == 0 else 0
        temp += 2 if N % 10 == 0 else 0
        temp += 4 if N % 25 == 0 else 0
        coins += [coins[-1] + temp]
        N += 1
    return coins[n]


# 8.12
def queen():
    seeds = [(x, 0) for x in range(8)]
    answer = []
    for x, y in seeds:
        queens1 = [(x, y)]
        queens2 = [(x, y)]
        a = x
        while y < 8:
            x = (x + 2) % 8
            y += 1
            queens1.append((x, y))
            a = (a + 4) % 8
            queens2.append((a, y))
        answer.extend([queens1, queens2])
    return answer
