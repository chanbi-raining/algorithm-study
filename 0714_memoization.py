# 알고리즘스터디 시즌 2
'''
- date: 2019-07-14, 2019-07-21, 2019-07-28
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


# 8.6
def _move(n, fro, to, via):
    if n == 1:
        to.append(fro.pop())
        return [fro, via, to]
    else:
        _move(n - 1, fro, via, to)
        to.append(fro.pop())
        return _move(n - 1, via, to, fro)
        
def hanoi(N):
    from collections import deque
    cols = [deque(), deque(), deque()]
    goals = deque()
    for i in range(1, N + 1):
        cols[0].appendleft(i)
        goals.appendleft(i)
    newcols = _move(N, cols[0], cols[2], cols[1])
    print(len(newcols[0]), len(newcols[1]), len(newcols[2]))
    if newcols[2] == goals:
        return True
    return False


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


# 8.10
def helpaint(area, pt, color, curr):
    a, b = pt
    if area[a][b] == curr:
        area[a][b] = color
        print((a, b), end=' ')
        if b - 1 >= 0:
            helpaint(area, (a, b-1), color, curr)
        if b + 1 < len(area[0]):
            helpaint(area, (a, b + 1), color, curr)
        if a - 1 >= 0:
            helpaint(area, (a - 1, b), color, curr)
        if a + 1 < len(area):
            helpaint(area, (a + 1, b), color, curr)
        return area

def paintfill(area, pt, color):
    a, b = pt
    curr = area[a][b]
    if curr == color: return area
    return helpaint(area, (a, b), color, curr)


# 8.11
def cntcoin(n):
    lst = [1] * (n + 1)
    for coin in [5, 10, 25]:
        for idx in range(n + 1):
            lst[idx] += lst[idx - coin] if (idx - coin) >= 0 else 0
    return lst[n]


# 8.12
def queen(lst):
    # findQ's helper function
    if len(lst) == 8:
        print(lst)
    a = lst[-1][0] + 1
    nott = [x[1] for x in lst] + [sum(x) - a for x in lst] + [x[1] - x[0] + a for x in lst]
    new = list(filter(lambda x: x not in nott, range(8)))
    if not new:
        return
    for i in new:
        queen(lst + [(a, i)])        
        
def findQ():
    seeds = [(0, x) for x in range(8)]
    for seed in seeds:
        queen([seed])


# 8.13 - input in (w, h, d)
def stackbox(boxes): 
    boxes = [(x[1], x[0], x[2]) for x in boxes]
    boxes.sort(reverse=True)
    return helpstack(boxes)
    
def helpstack(boxes):
    if not boxes: return 0
    if len(boxes) == 1:
        return boxes[0][0]
    h, w, d = boxes[0][0], boxes[0][1], boxes[0][2]
    newbox = list(filter(lambda x: x[0] < h and x[1] < w and x[2] < d, boxes[1:]))
    return max(helpstack(boxes[1:]), h + helpstack(newbox))