'''
Learning Python 4th Edition
Created on Apr 30, 2016

@author: eddy
String representation: __str__ and __repr
'''

class Printer:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return str(self.val)
    
    
obj = [Printer(2), Printer(3)]
for x in obj:
    print(x)
