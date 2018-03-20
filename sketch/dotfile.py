#!/usr/bin/env python
#from 

#with open("filename", "r") as f:
#    for l in f.read():
#        if l.isupper():
#            print(l)
#print([l for l in open("filename", "r")])
print([x for x in line.strip() for line in open("filename", "r")])
