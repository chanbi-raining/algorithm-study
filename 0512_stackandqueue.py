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
        cursor = self.top
        string = str(cursor.data)
        cursor = cursor.next
        while cursor:
            string +=  '->' + str(cursor.data)
            cursor = cursor.next
        return string