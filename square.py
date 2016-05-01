#!/usr/bin/python3
#Learning Python 4th Edition


class Square:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        self.start += 1
        return self.start ** 2
    
def main():
        for i in Square(1, 5):
            print(i, end=' ')

            
if __name__ == '__main__': 
    main()