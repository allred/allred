#!/usr/bin/env python
import json


class EmptyNode():
    def insert(self, v):
        return None

    def search(self, v):
        return False


class Node():
    def __init__(self, v):
        self.value = v
        self.left = EmptyNode()
        self.right = EmptyNode()

    def insert(self, v):
        if v < self.value:
            self.left = Node(v)
        elif v > self.value:
            self.right = Node(v)
        else:
            return False

    def search(self, v):
        if v < self.value:
            return self.left.search(v)
        elif v > self.value:
            return self.right.search(v)
        else:
            return True


tree = Node(5)
tree.insert(7)
tree.insert(3)
print(tree.__dict__)
print(tree.search(3))
