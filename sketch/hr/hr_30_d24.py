#!/usr/bin/env python
# remove dupes from linked list
import sys
import io 

oldstdin = sys.stdin
text = '''6
1
2
2
3
3
4
'''
sys.stdin = io.StringIO(text)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self,head):
        if not hasattr(self, 'head'):
            self.head = head
        if head == None or head.next == None:
            return self.head
        if head.data == head.next.data:
            head.next = head.next.next
            return self.removeDuplicates(head)
        else:
            return self.removeDuplicates(head.next)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head)
