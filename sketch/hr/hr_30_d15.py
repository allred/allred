#!/usr/bin/env python
# linked list
import sys
import io 

oldstdin = sys.stdin
text = '''4
2
3
4
1
'''
sys.stdin = io.StringIO(text)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        if head == None:
            node = Node(data)
            return node
        current = head
        while current.next != None:
            current = current.next
        current.next = Node(data)
        return head 

mylist = Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 
