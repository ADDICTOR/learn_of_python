class Array():
    def __init__(self,size=4):
        self.__size = size  # 记录容器大小
        self.__item = [None]*size  # 分配空间
        self.__length = 0
    
    def __setitem__(self,key,value):
        self.__item[key] = value
        self.__length += 1

    def __getitem__(self,key):
        return self.__item[key]
    
    def __len__(self):
        return self.__length
    
    def __iter__(self):
        for value  in self.__item:
            yield value
class Queue():
    def __init__(self,size=4):
        self.item = Array(size)
        self.size = size
        self.head = 0
        self.end = 0
    def put(self,value):
        self.item[self.head % self.size] = value
        self.head += 1
    def pop(self):
        temp =  self.item[self.end % self.size]
        self.end += 1
        return temp

if __name__ == "__main__":
    q = Queue()
    q.put('曹操')
    q.put('刘备')
    q.put('孙权')

    print(q.pop())
    print(q.pop())
    print(q.pop())