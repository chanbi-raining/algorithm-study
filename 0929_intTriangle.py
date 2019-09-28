# 알고리즘스터디 시즌 3
'''
- date: 2019-09-29
- participants: @yoonjoo-pil, @cjttkfkd3941 
'''

# 백준 1932번 정수 삼각형 (DP)

import sys

def triangle_maxsum(triangle, N):
    summ = triangle[0]
    for i in range(1, N):
        summ = _maxsum(summ, triangle[i])
    return max(summ)

def _maxsum(summ, row):
    tmp = [0] * len(row)
    for idx, num in enumerate(summ):
        tmp[idx] = max(summ[idx] + row[idx], tmp[idx])
        tmp[idx + 1] = max(summ[idx] + row[idx + 1], tmp[idx + 1])
    return tmp

N = int(sys.stdin.readline())
triangle = [[]] * N
for i in range(N):
    triangle[i] = [int(x) for x in sys.stdin.readline().split()]
print(triangle_maxsum(triangle, N))



# 백준 11660번 구간 합 구하기 5

read = sys.stdin.readline

def range_sum(a, b, c, d, square):
    summ = 0
    for i in range(a - 1, c):
        for j in range(b - 1, d):
            summ += square[i][j]
    return summ

N, M = tuple(map(int, read().split()))
square = [[0] * N for _ in range(N)]
ans = [0] * M
for i in range(N):
    square[i] = list(map(int, read().split()))
for i in range(M):
    print(range_sum(*tuple(map(int, read().split())), square))
    

# 백준 2517번 달리기

def best_place():
    N = int(read())
    lst = [int(read())]
    print(1)
    for i in range(1, N):
        tmp = int(read())
        front = i
        end = 0
        if lst[0] > tmp > lst[-1]:
            while front > end:
                mid = (front + end) // 2
                if lst[mid] > tmp:
                    end = mid + 1
                else:
                    front = mid
        elif lst[-1] > tmp:
            end = len(lst)
        else:
            end = 0
        print(end + 1)
        lst = lst[:end] + [tmp] + lst[end:]
    
best_place()
