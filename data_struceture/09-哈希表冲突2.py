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
    def __init__(self,key = None,value = None,next = None):
        self.key = key
        self.value = value
        self.next = next
    def __str__(self):
        return 'key: {} value: {}'.format(self.key,self.value)

class HashTable():
    def __init__(self):
        self.size = 4
        self.items = Array(self.size)
    def get_index(self,key):
        return hash(key) % self.size

    def put(self,key,value): # 存放数据
        s = Slot(key,value) # 封装slot节点
        index = self.get_index(key) # 获取默认的索引位置
        # 索引位置是空的
        if self.items[index] == None:
            self.items[index] = s  # 直接赋值
        else:# 索引位置是非空的
            # 所占空间的数据的key 与 传入数据 key 相同
            if self.items[index].key == key:
                self.items[index].value = value
            else: # 所占空间的数据的key 与 传入数据 key 不相同
                temp = self.items[index] # 记录当前节点
                temp_next = self.items[index].next # 记录下一个节点
                while temp_next is not None:
                    if temp_next.key == key:
                        temp_next.value = value  # 更新原来节点的数据
                        return
                    temp = temp_next
                    temp_next= temp.next 
                temp.next = s

    def get(self,key): # 获取数据
        index = self.get_index(key)
        if self.items[index]:
            if self.items[index].key == key:
                return self.items[index].value
            else:
                temp_next = self.items[index].next
                while temp_next is not None:
                    if temp_next.key == key:
                        return temp_next.value
                    temp_next = temp_next.next
                return None
        return None
if __name__ == "__main__":
    h = HashTable()
    h.put('name','吕布')
    h.put('sex1','男')
    h.put('sex2','女')
    h.put('sex3','保密')

    print(h.get('name'))
    print(h.get('sex3'))
    print(h.get('sex2'))
    print(h.get('sex1'))
  