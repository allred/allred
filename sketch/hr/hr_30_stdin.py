#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''3
2
1
'''
sys.stdin = io.StringIO(text)
print(input().strip())
