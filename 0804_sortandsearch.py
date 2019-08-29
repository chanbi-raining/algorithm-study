# 알고리즘스터디 시즌 2
'''
- date: 2019-08-04, 2019-08-17
- participants: @yoonjoo-pil, @cjttkfkd3941
- chapter(s): Sorting and Searching
'''

# 10.1
def sortNmerge(A, B):
    alen, blen = len(A), len(B)
    for aid in range(alen - blen - 1, -1, -1):
        if aid != None and aid != 0:
            break
    bid, cur = blen - 1, alen - 1
    
    while aid >= 0 and bid >= 0:
        if A[aid] >= B[bid]:
            A[cur] = A[aid]
            aid -= 1
        else:
            A[cur] = B[bid]
            bid -= 1
        cur -= 1
            
    if bid != 0:
        for i in range(bid + 1):
            A[i] = B[i]
    return A


# 10.2
def anasort(lst):
    N = len(lst)
    newlst = [(''.join(sorted(lst[i])), lst[i]) for i in range(N)]
    newlst.sort()
    return [newlst[x][1] for x in range(N)]


# 10.3
def rotatesearch(lst, elem): # O(n)
    n = len(lst)
    maxidx = lst.index(max(lst))
    minidx = maxidx + 1 if maxidx != n - 1 else 0 
    newlst = lst[minidx:] + lst[:maxidx]
    newidx = binarysearch(newlst, elem)
    answer = newidx + minidx if elem < lst[0] else newidx - minidx
    return newidx + minidx if newidx + minidx < n else newidx + n - minidx

def binarysearch(lst, elem):
    start, end = 0, len(lst) - 1
    while start < end:
        idx = (start + end) // 2
        if lst[idx] == elem:
            return idx
        if lst[idx] < elem:
            start = idx + 1
        else:
            end = idx - 1
    return -1

def rotatesearch2(lst, elem):
    N = len(lst)
    start, end =  0, N - 1
    while start < end:
        idx = (start + end) // 2
        if lst[idx] == elem:
            return idx
        if lst[start] <= elem < lst[idx] or elem > lst[end]:
            end = idx - 1
            continue
        # elem <= lst[start] or lst[idx] < elem <= lst[end]
        start = idx + 1
    return start if lst[start] == elem else -1


# 10.4
class Listy():
    def __init__(self, lst):
        self.lst = lst
    
    def elementAt(self, i):
        return self.lst[i] if i < len(self.lst) else -1
    
def findidx(listy, x):
    start = idx = 0
    while True:
        temp = listy.elementAt(2 ** idx)
        if temp == x: return 2 ** idx
        if temp == -1 or temp > x:
            end = 2 **idx
            break
        elif temp < x:
            start = 2 ** idx
        idx += 1
    
    while start < end:
        idx = (start + end) // 2
        if listy.elementAt(idx) == x:
            return idx
        if listy.elementAt(idx) == -1 or listy.elementAt(idx) > x:
            end = idx - 1
        else:
            start = idx + 1
    return -1


# 10.5
def binarystrsearch(elem, lst):
    start, end = 0, len(lst) - 1
    while start < end:
        idx = (start + end) // 2
        left = idx - 1
        right = idx + 1
        while not lst[idx]:
            if left < start and right > end: return -1
            if left >= start and lst[left]: idx = left
            elif right <= end and lst[right]: idx = right
            else:
                left -= 1
                right += 1
        if lst[idx] == elem:
            return idx
        if lst[idx] < elem:
            start = idx + 1
        else:
            end = idx - 1
    return -1


# 10.9
def matrix_search(mat, elem):
    from collections import deque
    M = len(mat)
    N = len(mat[0])
    
    top, left = 0, 0
    bottom, right = M - 1, N - 1
    temp = deque()
    check = set()
    
    while True:
        if top <= bottom and left <= right:
            check.add((top, bottom, left, right))
            x, y = (top + bottom) // 2, (left + right) // 2
            if mat[x][y] == elem:
                return x, y
            if mat[x][y] < elem:
                t1 = (x + 1, bottom, left, right)
                t2 = (top, bottom, y + 1, right)
                if t1 not in check: temp.append(t1)
                if t2 not in check: temp.append(t2)
            elif mat[x][y] > elem:
                t3 = (top, x + 1, left, right)
                t4 = (top, bottom, left, y + 1)
                if t3 not in check: temp.append(t3)
                if t4 not in check: temp.append(t4)

        if not temp: break
        top, bottom, left, right = temp.pop()
    
    return -1


# 10.11
def peakvalley(lst):
    N = len(lst)
    i = 0
    while i + 2 < N:
        temp = [lst[i], lst[i + 1], lst[i + 2]]
        if max(temp) != lst[i + 1]:
            print(i)
            tmp = lst.index(max(temp))
            lst[tmp], lst[i + 1] = lst[i + 1], lst[tmp]
        i += 2
    return lst
