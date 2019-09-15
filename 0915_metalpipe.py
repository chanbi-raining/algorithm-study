# 알고리즘스터디 시즌 3
'''
- date: 2019-09-15
- participants: @yoonjoo-pil, @cjttkfkd3941 
'''
# 01 programmers - 쇠막대기 (스택/큐)
# https://programmers.co.kr/learn/courses/30/lessons/42585

def solution(arrangement):
    answer = 0
    openn = 0
    flag = 0
    for char in arrangement:
        if char == '(':
            openn += 1
            answer += 1
            flag = 1
        elif char == ')':
            openn -= 1
            if flag == 1:
                answer += openn - 1
            flag = 0
    return answer


# 02 programmers - 주식가격 (스택/큐)
# https://programmers.co.kr/learn/courses/30/lessons/42584 

def solution(prices):
    N = len(prices)
    answer = [0 for i in range(N)]
    for idx in range(N - 1):
        tmp = prices[idx]
        for p in range(idx, N):
            if prices[p] < tmp:
                break
        answer[idx] = p - idx
    return answer


# 03 programmers - 등굣길 (DP)
# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    div = 1000000007
    mat = [[0] * (n + 1) for i in range(m + 1)]
    mat[1][1] = 1
    for x, y in puddles:
        mat[x][y] = None
    for a in range(1, m + 1):
        for b in range(1, n + 1):
            if not mat[a][b]: continue
            if a + 1 <= m and mat[a + 1][b] is not None:
                mat[a + 1][b] += mat[a][b] % div
            if b + 1 <= n and mat[a][b + 1] is not None:
                mat[a][b + 1] += mat[a][b] % div
    return mat[m][n] % div
