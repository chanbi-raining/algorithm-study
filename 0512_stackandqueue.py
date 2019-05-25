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
        self.minn = Stack()
    
    def push(self, data):
        self.size += 1
        if self.top:
            self.top = StackNode(data, self.top)
            if self.minn.peek() > data:
                self.minn.push(data)
        else:
            self.top = StackNode(data)
            self.minn.push(data)
    
    def pop(self):
        if self.top:
            self.size -= 1
            temp = self.top.data
            self.top = self.top.next
            if self.minn.peek() ==  temp:
                self.minn.pop()
            return temp
        else:
            print('\tthe stack is empty')
    
    def min(self):
        if self.minn:
            return self.minn.peek()
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
    

def sortStack(example):
    tempstack = Stack()
    tempstack.push(example.pop())
    while not example.isEmpty():
        if tempstack.peek() < example.peek():
            tempstack.push(example.pop())
        else:
            temp = example.pop()
            while not tempstack.isEmpty():
                example.push(tempstack.pop())
            tempstack.push(temp)
    while not tempstack.isEmpty():
        example.push(tempstack.pop())
    return example
    

class AnimalNode():
    def __init__(self, name, order, nextt=None):
        self.data = name
        self.next = nextt
        self.order = order
        
class AnimalQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def add(self, data, order):
        if self.first:
            self.last.next = AnimalNode(data, order)
            self.last = self.last.next
        else:
            self.first = self.last = AnimalNode(data, order)
    
    def timestamp(self):
        return self.first.order

class AnimalShelter():
    def __init__(self):
        self.cats = AnimalQueue()
        self.dogs = AnimalQueue()
        self.order = 0
    
    def enqueue(self, name, species):
        if species == 'cat':
            self.cats.add(name, self.order)
        else:
            self.dogs.add(name, self.order)
        self.order += 1
    
    def dequeueAny(self):
        if self.cats and self.dogs:
            if self.cats.timestamp() > self.dogs.timestamp():
                return self.dogs.remove()
            return self.cats.remove()
        if self.cats:
            return self.cats.remove()
        if self.dogs:
            return self.dogs.remove()
        return 'No animals left'
    
    def dequeueDog(self):
        return self.dogs.remove()
    
    def dequeueCat(self):
        return self.cats.remove()
