# 알고리즘 시즌 2
'''
- date: 2019-05-12
- participants: @yoonjoo-pil, @cjttkfkd3941
- chapters: Stack and Queue
'''

# implementing stack in python
class StackNode():
    def __init__(self, data, nextt=None):
        self.data = data
        self.next = nextt


class Stack():
    def __init__(self):
        self.size = 0
        self.top = None
    
    def isEmpty(self):
        return bool(self.size == 0)
    
    def push(self, data):
        self.size += 1
        if self.top:
            self.top = StackNode(data, self.top)
        else:
            self.top = StackNode(data)
    
    def pop(self):
        if self.top:
            self.size -= 1
            temp = self.top.data
            self.top = self.top.next
            return temp
        else:
            print('\tthe stack is empty')
    
    def peek(self):
        if self.isEmpty():a
            print('\tthe stack is empty')
            return
        return self.top.data
    
    def __str__(self):
        if not self.top:
            print('\tthe stack is empty')
        return
        cursor = self.top
        string = str(cursor.data)
        cursor = cursor.next
        while cursor:
            string +=  '->' + str(cursor.data)
            cursor = cursor.next
        return string        

# implementing queue in python    
class QueueNode():
    def __init__(self, data, nextt=None):
        self.data = data
        self.next = nextt
    

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, data):
        if self.first:
            self.last.next = QueueNode(data)
            self.last = self.last.next
        else:
            self.first = self.last = QueueNode(data)
        
    def remove(self):
        if self.first:
            temp = self.first.data
            self.first = self.first.next
            return temp
        print('\tthe queue is empty')
        return        
    
    def peek(self):
        if self.first:
            return self.first.data
        print('\tthe queue is empty')
        return
    
    def isEmpty(self):
        return bool(self.first)

# 3.2
class Stack32(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.minn = None
    
    def push(self, data):
        self.size += 1
        if self.top:
            self.top = StackNode(data, self.top)
            if self.minn.data > self.top.data:
                self.minn = self.top
        else:
            self.top = StackNode(data)
            self.minn = self.top
    
    def pop(self):
        if self.top:
            self.size -= 1
            if self.minn == self.top and self.size == 0:
                self.minn = None
            elif self.minn == self.top:
                pointer = self.top.next
                self.minn = self.top.next
                while pointer:
                    if self.minn.data > pointer.data:
                        self.minn = pointer
                    pointer = pointer.next
            temp = self.top.data
            self.top = self.top.next
            return temp
        else:
            print('\tthe stack is empty')

    def min(self):
        if self.minn:
            return self.minn.data
        print('\tthe stack is empty')
        return
    
# 3.3
class Stack33(Stack):
    def __init__(self, nextStack=None):
        Stack.__init__(self)
        self.nextStack = nextStack
        
class SetOfStacks():
    def __init__(self, sizelimit=10):
        self.sizelimit = sizelimit
        self.top = None
    
    def push(self, data):
        if not self.top:
            self.top = Stack33()
        elif self.top.size >= self.sizelimit:
            self.top = Stack33(self.top)
        self.top.push(data)
    
    def pop(self):
        if not self.top:
            print('No node')
            return
        temp = self.top.pop()
        if self.top.size == 0:
            self.top = self.top.nextStack
        return temp
    
    def __str__(self):
        if not self.top:
            print('No node')
            return
        cursor1 = self.top
        string = ''
        while cursor1:
            cursor2 = cursor1.top
            while cursor2:
                string += '->' + str(cursor2.data)
                cursor2 = cursor2.next
            string += ' // '
            cursor1 = cursor1.nextStack
        return string

# 3.4
class MyQueue():
    def __init__(self):
        self.origin = Stack()
        self.temp = Stack()
    
    def add(self, data):
        self.origin.push(data)
    
    def remove(self):
        while not self.origin.isEmpty():
            self.temp.push(self.origin.pop())
        temp = self.temp.pop()
        while not self.temp.isEmpty():
            self.origin.push(self.temp.pop())
        return temp
    
    def peek(self):
        while not self.origin.isEmpty():
            self.temp.push(self.origin.pop())
        temp = self.temp.pop()
        self.origin.push(temp)
        while not self.temp.isEmpty():
            self.origin.push(self.temp.pop())
        return temp
    
    def isEmpty(self):
        return self.origin.isEmpty()
    
# 3.5
class SmallStack():
    def __init__(self):
        self.min = None
    
    def push(self, data):
        if not self.min:
            self.min = StackNode(data)
        elif self.min.data > data:
            self.min = StackNode(data, self.min)
        else:
            cursor = self.min
            while cursor.next and cursor.next.data < data:   
                cursor = cursor.next
            cursor.next = StackNode(data, cursor.next)
    
    def pop(self):
        if self.min:
            temp = self.min.data
            self.min = self.min.next
            return temp
        return 'No node'
        
    def peek(self):
        if self.min:
            return self.min
        return 'No node'
    
    def isEmpty(self):
        return not bool(self.min)
    
    def __str__(self):
        if not self.min:
            print('\tthe stack is empty')
        cursor = self.min
        string = str(cursor.data)
        cursor = cursor.next
        while cursor:
            string +=  '->' + str(cursor.data)
            cursor = cursor.next
        return string
    
    
