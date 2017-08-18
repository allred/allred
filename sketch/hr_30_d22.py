#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''7
3
5
2
1
4
6
7
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

    def getHeight(self,root):
        if root is None:
            return -1
        else:
            hl = self.getHeight(root.left)
            hr = self.getHeight(root.right)
            if hl > hr:
                return hl + 1
            else:
                return hr + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
