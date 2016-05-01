'''
Learning Python 4th Edition
Created on Apr 30, 2016

@author: eddy
Call expression: __call__
'''

class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)
        
c = Callee()
