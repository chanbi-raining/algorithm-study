# 알고리즘 시즌 2
'''
- date: 2019-05-26, 2019-06-09
- participants: @yoonjoo-pil, @cjttkfkd3941
- chapters: Trees and Graphs
'''

# 4.1
class GraphNode():
    def __init__(self, value=None):
        self.visited = False
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
def find_path(graph, n1, n2):
    from collections import deque
    flag = False
    checknode = [n1, n2]
    checkdeque = [deque(), deque()]
    for idx in range(2):
        if checknode[idx] in graph:
            flag = True
            for link in graph[checknode[idx]]:
                checkdeque[idx].append(link)
    if flag == False:
        return False

    for idx in range(2):
        c_deque, c_node = checkdeque[idx], checknode[1 - idx]
        while c_deque:
            temp = c_deque.pop()
            if temp.visited == True: continue
            temp.visited = True
            if temp == c_node:
                return True
            if temp in graph:
                for link in graph[temp]:
                    c_deque.append(link)
    return False

'''
# test code
if __name__ == '__main__':
    v0 = GraphNode(0)
    v1 = GraphNode(1)
    v2 = GraphNode(2)
    v3 = GraphNode(3)
    v4 = GraphNode(4)
    v5 = GraphNode(5)

    graph = {v0: [v1, v4, v5], v1: [v3, v4], v2: [v3], v3: [v2, v4]}
    test41_a = find_path(graph, v0, v4)
    test41_b = find_path(graph, v1, v5)
    print(test41_a == True)
    print(test41_b == True)
'''

# 4.2
class BTNode():
    def __init__(self, value, parent=None, leftchild=None, rightchild=None):
        self.value = value
        self.parent = parent
        self.leftchild = leftchild
        self.rightchild = rightchild

    def insertValue(self, nodeval):
        if self.value < nodeval:
            if self.rightchild:
                self.rightchild.insertValue(nodeval)
            else:
                self.rightchild = BTNode(nodeval, parent=self)
        elif self.leftchild:
            self.leftchild.insertValue(nodeval)
        else:
            self.leftchild = BTNode(nodeval, parent=self)

    def insertNode(self, node):
        if self.value < node.value:
            if not self.rightchild:
                self.rightchild = node
                node.parent = self
            else:
                self.rightchild.insertNode(node)
        elif not self.leftchild:
            self.leftchild = node
            node.parent = self
        else:
            self.insertNode(node)

    def createMinimalTree(self, lst):
        if len(lst) <= 2:
            while lst:
                self.insertValue(lst.pop())
        else:
            mid = len(lst) // 2
            subhead = BTNode(lst[mid])
            subhead.createMinimalTree(lst[:mid])
            subhead.createMinimalTree(lst[mid + 1:])
            self.insertNode(subhead)

    def string(self):
        left, right = None, None
        if self.leftchild:
            left = self.leftchild.string()
        if self.rightchild:
            right = self.rightchild.string()
        if left == None and right == None:
            return self.value
        return [self.value, [left, right]]

    def __str__(self):
        return str(self.string())


def make_bst(lst):
    mid = len(lst) // 2
    head = BTNode(lst[mid])
    head.createMinimalTree(lst[:mid])
    head.createMinimalTree(lst[mid + 1:])
    return head 

# 4.3
def bfs(head):
    from collections import deque
    tree = deque()
    tree.append((head, 0))
    answer = []
    while tree:
        node, layer = tree.popleft()
        if len(answer) >= layer + 1:
            answer[layer] += [node.value]
        else:
            answer.append([node.value])
        if node.leftchild: tree.append((node.leftchild, layer + 1))
        if node.rightchild: tree.append((node.rightchild, layer + 1))
    return answer

'''
# test code
if __name__ == '__main__':
    head = make_bst(list(range(1, 11)))
    print(head)
    print(bfs(head))
'''

# 4.4
def hasChildren(node):
    if node:
        assert type(node) == BTNode
        return bool(node.leftchild or node.rightchild)
    return False

def checkbalance(head):
    if head.leftchild and head.rightchild:
        return checkbalance(head.leftchild) and checkbalance(head.rightchild)
    cursor = head.leftchild if head.leftchild else head.rightchild
    if not hasChildren(cursor):
        return True
    if hasChildren(cursor.leftchild) or hasChildren(cursor.rightchild):
        return False

'''
# test code
if __name__ == '__main__':
    print(checkbalance(make_bst(list(range(10)))) == True)
    print(checkbalance(make_bst([6, 2, 3, 1, 10, 9, 20])) == False)
'''

    
# 4.5
def isBST(head):
    # if head == leafnode
    if not hasChildren(head):
        return True
    
    if head.leftchild and head.rightchild:
        if not (hasChildren(head.leftchild) and hasChildren(head.rightchild)): 
            return bool(head.leftchild.value < head.value < head.rightchild.value) and isBST(head.leftchild) and isBST(head.rightchild)
    if head.leftchild:
        return bool(head.leftchild.value < head.value) and isBST(head.leftchild) 
    if head.rightchild:
        return bool(head.value < head.rightchild.value) and isBST(head.rightchild)
