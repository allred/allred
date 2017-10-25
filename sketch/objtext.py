#!/usr/bin/env python

class Sub:
  def foo():
    print("blah")


s = Sub
print(hasattr(s, 'foo'))
print(callable('s.foo'))
#print(s.dir)
if not hasattr(s, 'blah'):
  print("doesn't have blah")
