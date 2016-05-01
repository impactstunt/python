'''
Learning Python 4th Edition
Created on Apr 30, 2016

@author: eddy
In-Place Addition: __iadd__ += or __add__
'''

class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        self.val += other
        return self
    
x = Number(5)
x += 1
x += 1
print(x.val)

