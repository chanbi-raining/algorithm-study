# 알고리즘스터디 시즌 2
'''
- date: 2019-06-16
- participants: @yoonjoo-pil, @cjttkfkd3941
- chapter(s): Bit Manipulation
'''

# 5.1
def addMtoN(N, M, i, j, binary=True):
    if binary:
        N = int(str(N), 2)
        M = int(str(M), 2)
    # save i to last bits
    itolastN = N & (1 << i) - 1
    
    # delete j to last bits from N
    answer = N & ~((1 << j) - 1)
    
    # add M to ith position of N
    lenM = len(bin(M)[2:])
    shift = M << (j - lenM + 1)
    answer = answer | shift
    
    # add itolastN
    return int(bin(answer | itolastN)[2:])


# 5.2
def bin2str(N):
    if (N * (2 ** 30)) % 1  != 0:
        return False
    answer = '0.'
    while N != 0:
        N *= 2
        answer += str(int(N // 1))
        N = N % 1
    return answer

'''
# test code
if __name__ == '__main__':
    print(addMtoN(10000000000, 10011, 2, 6))
    print(addMtoN(11111111111, 10011, 2, 6))

    print(bin2str(0.5))
    print(bin2str(0.25))
    print(bin2str(0.125))
    print(bin2str(0.0625))
    print(bin2str(0.75))
    print(bin2str(0.72))
'''