# 알고리즘 시즌 2
'''
- date: 2019-04-29
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
        pass
                
exlink = linkedList()
print(exlink)
exlink.addToTail(4)
print(exlink)
exlink.addToTail(5)
print(exlink)
exlink.addToTail(6)
print(exlink)
exlink.deleteNode(4)
print(exlink)
exlink.deleteNode(6)
print(exlink)
exlink.deleteNode(5)
print(exlink)

'''
no node in the linked list
4
4 -> 5
4 -> 5 -> 6
5 -> 6
5
no node in the linked list
'''

# 2.1 eliminate duplicates

ex2link = linkedList()
for i in [1, 2, 1, 4, 5, 1, 1, 4, 7]:
    ex2link.addToTail(i)
print(ex2link)
ex2link.elimDup()
print(ex2link)

'''
1 -> 2 -> 1 -> 4 -> 5 -> 1 -> 1 -> 4 -> 7
1 -> 2 -> 4 -> 5 -> 7
'''