# 알고리즘스터디 시즌 3
'''
- date: 2019-09-22
- participants: @yoonjoo-pil, @cjttkfkd3941 
'''
# 01 백준 1912번 연속합
# https://www.acmicpc.net/problem/1912

def consecsum(lst):
    answer = max(lst)
    tmp = 0
    summ = lst[0]
    for i in lst:
        tmp += i
        summ = max(tmp, summ)
        answer = max(answer, summ)
        tmp = max(0, tmp)
    return answer

N = input()
lst = [int(x) for x in input().split()]
print(consecsum(lst))


# 02 백준 11053번 LIS
# https://www.acmicpc.net/problem/11053

def longest(lst, N):
    answer = [1] * N
    for j in range(1, N):
        for i in range(j):
            if lst[i] < lst[j] and answer[i] + 1 > answer[j]:
                answer[j] = answer[i] + 1
    return max(answer)

N = int(input())
print(longest([int(x) for x in input().split()], N))


# 03 백준 7453번 합이 0인 네 정수
# https://www.acmicpc.net/problem/7453

import sys
from itertools import product
def sumzero(A, B, C, D):
    result = 0
    CD = sorted([sum(x) for x in product(C, D)])
    for a in A:
        for b in B:
            upper = binarysearch(CD, - (a + b), True)
            lower = binarysearch(CD, - (a + b), False)
            cnt = upper - lower
            result += cnt
    return result

def binarysearch(CD, find, upper=True):
    start, end = 0, len(CD)
    while start < end:
        mid = (start + end) // 2
        if (upper and CD[mid] <= find) or ((not upper) and CD[mid] < find):
            start = mid + 1
        else:
            end = mid
    return end if upper else start
    
N = int(sys.stdin.readline())
nums = [[None] * 4 for _ in range(N)]
for i in range(N):
    nums[i][:] = list(map(int, sys.stdin.readline().split()))
nums = list(zip(*nums))
print(sumzero(*nums))
