# baekjoon 1158

def solution(N, K):
    idx = -1
    lst = list(range(1, N + 1))
    answer = []
    while True:
        idx += K
        if idx >= len(lst):
            idx -= len(lst) if idx >= len(lst) else 0
            lst = list(filter(lambda x: x != None, lst))
        if not lst: break
        idx %= len(lst)
        answer.append(lst[idx])
        lst[idx] = None
    return '<' + str(answer)[1:-1] + '>'
   
if __name__ == '__main__':
    N, K = [eval(x) for x in input().split()]
    print(solution(N, K))