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
        
    def addToTail(self, end):
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
            else:
                self.head = None
        else:
            pointer = self.head
            while pointer.next.data != nodedata:
                if pointer.next.next:
                    pointer = pointer.next
                else:
                    return 'no such data'
            pointer.next = pointer.next.next
            
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
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        if pointer.data in buffer:
            pointer = None

    def elimDup2(self): # without buffer
        if not self.head:
            return 'no node in the linked list'
        pointer = self.head
        while pointer and pointer.next:
            cursor = self.head
            cnt = int(cursor.data == pointer.data)
            while cursor and cursor.next:
                if cursor.next.data == pointer.data:
                    cnt += 1
                    if cnt >= 2:
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
    