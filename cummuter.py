'''
Learning Python 4th Edition
Created on Apr 30, 2016

@author: eddy
Right-side and in-place addition: __radd__ and __iadd__
'''

class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val
    
x = Commuter(88)
y = Commuter(99)

print(x + 1) # __add__: instance + instance
print(1 + y) # __radd__: non-instance + instance 
print(x + y) # __add__: instance + instance, triggers __radd__



