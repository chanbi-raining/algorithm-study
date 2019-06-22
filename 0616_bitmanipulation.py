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

# 5.3
def longest1(N):
    N = str(N)
    length = len(N)
    cnt = front = maxLen = 0
    for i in range(len(N)):
        if N[i] == '1':
            cnt += 1
        else:
            front += 1 if front != 0 else 0
            maxLen = max(maxLen, front + cnt)
            front = cnt if i + 1 != length and N[i + 1] == '1' else 0
            cnt = 0
    front += 1 if front != 0 else 0
    maxLen = max(front + cnt, maxLen)
    return maxLen

'''
# test code
if __name__ == '__main__':
    print(longest1(111111) == 6)
    print(longest1(1100000111000) == 3)
    print(longest1(1101110001) == 6)
    print(longest1(11011101111) == 8)
    print(longest1(11100001111) == 4)
    print(longest1(11011100011111111) == 8)
'''


# 5.6
def change2B(a, b):
    c = a ^ b
    count = 0
    while c != 0:
        c = c & (c - 1)
        count += 1
        print(bin(c))
    return count

'''
# test code
if __name__ = '__main__':
    print(change2B(29, 15) == 2)
'''

# 5.7
def swapBits(N):
    length = (len(bin(N)[2:]) + 3) // 4
    return  ((N & int('5' * length, 16)) << 1) + ((N & int('a' * length, 16)) >> 1)    