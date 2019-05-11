# 알고리즘 시즌 2
'''
- date: 2019-04-28 / 2019-05-02
- participants: @yoonjoo-pil, @cjttkfkd3941
- chapters: Linked List
'''

# implementing linked list in python

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addToTail(self, end):
        self.size += 1
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(end)
        else:
            self.head = Node(end)
            
    def deleteNode(self, nodedata):
        if self.head.data == nodedata:
            if self.head.next:
                self.head = self.head.next
                self.size -= 1
            else:
                self.head = None
                self.size = 0
        else:
            pointer = self.head
            while pointer.next.data != nodedata:
                if pointer.next.next:
                    pointer = pointer.next
                else:
                    return 'no such data'
            pointer.next = pointer.next.next
            self.size -= 1
            
    def __str__(self):
        if not self.head:
            return 'no node in the linked list'
        string = str(self.head.data)
        pointer = self.head
        while pointer.next:
            string += ' -> ' + str(pointer.next.data)
            pointer = pointer.next
        return string
    
    # 2.1
    def elimDup(self):
        if not self.head:
            return 'no node in the linked list'
        buffer = {self.head.data}
        pointer = self.head
        while pointer.next:
            buffer.add(pointer.data)
            if pointer.next.data in buffer:
                self.size -= 1
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
    
    def elimDup2(self):
        if not self.head:
            return 'no node in the linked list'
        pointer = self.head
        while pointer:
            cursor = self.head
            cnt = int(cursor.data == pointer.data)
            while cursor:
                if cursor.next.data == pointer.data:
                    cnt += 1
                if cnt >= 2:
                    self.size -= 1
                    if cursor.next.next:
                        cursor.next = cursor.next.next
                    else:
                        cursor.next = None
                cursor = cursor.next
            pointer = pointer.next
            
    # 2.2
    def size(self):
        return self.size
    
    def findNtolastelement(self, N):
        length = self.size
        pointer = self.head
        idx = 0
        if N > length:
            return 'N larger than size'
        if N <= 0:
            return 'N should be larger than 0'
        tofind = length - N
        while tofind != idx:
            pointer = pointer.next
            idx += 1
        return pointer.data
    
    def findNtolastelement2(self, N): # using 2 cursors
        cursor1 = self.head
        cursor2 = self.head
        cnt = 1
        while cursor2.next and cnt != N:
            cursor2 = cursor2.next
            cnt += 1
        while cursor2.next:
            cursor2 = cursor2.next
            cursor1 = cursor1.next
        return cursor1.data
    
     # 2.4
    def sendfront(self, N):
        newList = linkedList()
        cursor = self.head
        while cursor:
            newList.addToTail(cursor.data)
            cursor = cursor.next
        self.head = None
        self.size = 0
        cursor = newList.head
        while cursor:
            if cursor.data < N:
                self.addToTail(cursor.data)
                newList.deleteNode(cursor.data)
            cursor = cursor.next
        cursor = newList.head
        while cursor:
            self.addToTail(cursor.data)
            cursor = cursor.next
        return
    
    # 2.5 
    def addition(self, lst): # recursively
        summ = LinkedList._add(self.head, 0) + LinkedList._add(lst.head, 0)
        print(summ)
        new = LinkedList()
        numlst = [eval(i) for i in str(summ)]
        iterlst = range(len(numlst) - 1, -1, -1)
        for num in iterlst:
            new.addToTail(numlst[num])
        return new
    
    @staticmethod
    def _add(cursor, pos):
        value = 0 if not cursor else cursor.data * (10 ** (pos)) + LinkedList._add(cursor.next, pos + 1)
        return value
    
    # 2.6 
    def ispalindrome(self): # using stack
        length = self.size
        iteration = length // 2
        cursor = self.head
        stack = []
        for idx in range(iteration):
            stack.append(cursor.data)
            cursor = cursor.next
        if length % 2 == 1:
            cursor = cursor.next
        for idx in range(iteration):
            if cursor.data != stack.pop():
                return False
            cursor = cursor.next
        return True