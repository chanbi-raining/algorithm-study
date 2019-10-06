# 알고리즘스터디 시즌 3
'''
- date: 2019-10-06
- participants: @yoonjoo-pil, @cjttkfkd3941 
'''

import sys
read = sys.stdin.readline

# 백준 6603번 로또 (brute force)
# 1
from itertools import combinations

while True:
    lst = list(map(int, read().split()))
    if len(lst) == 1: break
    if flg == 1: print()
    k, S = lst[0], lst[1:]
    
    tmp = list(combinations(S, 6))
    for i in tmp:
        print(*i)
    print()

# 2
def listup(rest, tmp=tuple()):
    if len(tmp) == 6:
        return print(*tmp)
        
    if len(tmp) == 5 and len(rest) == 1:
        return print(*tmp, rest[0])
        
    if len(rest) > 1:
        listup(rest[1:], (*tmp, rest[0]))
        listup(rest[1:], tmp)

while True:
    lst = list(map(int, read().split()))
    if len(lst) == 1: break
    k, S = lst[0], lst[1:]
    listup(S)
    print()

    
# 백준 11049번 행렬 곱셈 순서 (DP)

def minmul(lst, N):
    mat = [[0] * N for _ in range(N)]
    for p in range(1, N):
        for i in range(N - p):
            j = i + p
            if i == j: continue
            mat[i][j] = 2 ** 31 - 1
            for k in range(i, j):
                tmp = mat[i][k] + mat[k + 1][j] + lst[i] * lst[k + 1] * lst[j + 1]
                mat[i][j] = min(mat[i][j], tmp)

    return mat[0][-1]

N = int(read())
lst = [None] * (N + 1)
lst[0], lst[1] = map(int, read().split())
if N == 1:
    print(0)
elif N > 1:
    for i in range(1, N):
        _, lst[i + 1] = map(int, read().split())
    print(minmul(lst, N))

