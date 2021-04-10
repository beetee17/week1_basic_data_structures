# python3

import sys
import threading

class Node():
    def __init__(self):
        self.parent = None
        self.children = []

    def get_parent(self):
        return self.parent
    def get_children(self):
        return self.children

    def add_parent(self, parent):
        self.parent = parent
    def add_child(self, child):
        self.children.append(child)

    

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def get_tree(n, parents):
    tree = [Node() for i in range(n)]
    for i in range(n):
        tree[i].add_parent(parents[i])

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].add_child(i)
    return tree, root

def get_height(n, parents):

    tree, root_index = get_tree(n, parents)
    height = 1
    Q = [tree[root_index]]
   
    while len(Q) > 0:
        
        next_Q = [] 
        for node in Q:
            for child in node.get_children():
                next_Q.append(tree[child]) # pre-queue all nodes of subsequent level
        
        if len(next_Q) > 0:
            height += 1
            Q = next_Q
             # deque and add nodes
       
        else:
            return height

    

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(get_height(n, parents))

    # n = 5
    # parents =[4, -1, 4, 1, 1]
    # tree, root = get_tree(n, parents)
    # print(get_height(tree, tree[root]))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
