#!/usr/bin/env python
# regex
import sys
import io 

oldstdin = sys.stdin
text = '''6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
'''
sys.stdin = io.StringIO(text)
N = int(input().strip())
names = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    import re
    if re.search(r'@gmail.com$', emailID) is not None:
        names.append(firstName)
print("\n".join(sorted(names)))
