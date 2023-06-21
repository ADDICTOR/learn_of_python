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

class Slot():
    def __init__(self,key = None,value = None):
        self.key = key
        self.value = value
    def __str__(self):
        return 'key: {} value: {}'.format(self.key,self.value)

class HashTable():
    def __init__(self):
        self.size = 4
        self.items = Array(self.size)
    def get_index(self,key):
        return hash(key) % self.size
    def put(self,key,value): # 存放数据
        s = Slot(key,value) 
        index = self.get_index(key)  # 获取key对应的索引
        self.items[index] = s
    def get(self,key): # 获取数据
        index = self.get_index(key) # 获取key对应的索引
        return self.items[index]
  
if __name__ == "__main__":
    h = HashTable()
    h.put('name','吕布')
    h.put('sex','男')

    print(h.get('name'))
    print(h.get('sex'))
  