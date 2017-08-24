#!/usr/bin/env python
# binary tree level-order traversal
import sys
import io 

oldstdin = sys.stdin
text = '''6
3
5
4
7
2
1
'''
sys.stdin = io.StringIO(text)
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #from collections import deque
        if not hasattr(self, 'queue'):
            #self.queue = deque([])
            self.queue = []
        if root is not None:
            self.queue.append(root)
            for i, tree in enumerate(self.queue):
                #tree = self.queue.popleft()
                #tree = self.queue.pop()
                print("{} ".format(tree.data), end='')
                if tree.left:
                    self.queue.append(tree.left)
                if tree.right:
                    self.queue.append(tree.right)
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
