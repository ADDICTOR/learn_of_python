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
        self.length =0 
    def get_index(self,key):
        return hash(key) % self.size
    def find_index_to_insert(self,key):
        index = self.get_index(key)  # 获取key对应的索引
        if self.items[index] == None:
            return index
        else:
            while self.items[index] is not None:
                if self.items[index].key == key: # 获取到相同的key
                    return index
                else:
                    index = (5*index+1)% self.size
            return index
    def put(self,key,value): # 存放数据
        s = Slot(key,value) 
        index = self.find_index_to_insert(key)  # 获取key对应的索引
        self.items[index] = s
        self.length += 1
        if self.load_factor():
            self.rehash()
    
    # 判断是否该扩容-装载因子
    def load_factor(self):
        return self.length /float(self.size) > 0.8
    # 扩充原来的空间大小-重哈希
    def rehash(self):
        # 保存原来的数据
        old = self.items
        # 设置新分配空间的大小
        self.size = self.size << 1
        # 分配新的空间
        self.items = Array(self.size)
        # 重置元素个数
        self.length = 0
        # 将原空间里的数据 放到新空间
        for s in old:
            if s:
                key = s.key 
                index = self.find_index_to_insert(key)
                self.items[index] = s
                self.length += 1

    def find_key(self,key):
        index = self.get_index(key)  # 获取key对应的索引
        if self.items[index] == None:
            return None
        else:
            while self.items is not None:
                if key == self.items[index].key: # 判断查找的Key是否与item里的key相同
                    return index
                else:
                    index = (5*index+1)% self.size
            return None
    def get(self,key): # 获取数据
        index = self.find_key(key) # 获取key对应的索引
        return self.items[index]
  
if __name__ == "__main__":
    h = HashTable()
    h.put('name','吕布')
    h.put('sex1','男')
    h.put('sex2','女')
    h.put('sex3','保密')
    h.put('sex4','保密110')

    print(h.get('name'))
    print(h.get('sex3'))
    print(h.get('sex2'))
    print(h.get('sex1'))
    print(h.get('sex4'))
  