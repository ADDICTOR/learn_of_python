from collections import deque

class Stack():
    def __init__(self):
        self.item = deque()
    
    def put(self,value):
        self.item.append(value)
    def pop(self):
        return self.item.pop()

    def pop2(self):
        return self.item.popleft()

if __name__ == "__main__":
    s = Stack()
    s.put('董卓')
    s.put('吕布')
    s.put('貂蝉')
    
    print(s.pop2())
    print(s.pop2())
    print(s.pop2())