# 알고리즘 시즌 2
'''
- date: 2019-05-26
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
