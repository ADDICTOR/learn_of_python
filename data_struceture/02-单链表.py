class Node():
    def __init__(self,value=None,next=None):
        self.value = value 
        self.next = next
    def __str__(self):
        return 'Node:{}'.format(self.value)
class LinkedList():
    def __init__(self):
        self.root = Node()
        self.size = 0 #记录有多少元素
        self.next = None  #增加新数据时，将新数据的地址与谁关联
    
    def append(self,value):
        node = Node(value)
        # 判断是否已经有数据
        if not self.next: #如果没有节点时
            self.root.next = node #将新节点挂到root后面
        else:
            self.next.next = node #将新节点挂到最后一个节点上
        self.next = node
        self.size += 1
    def append_first(self,value):
        node = Node(value)
        if not self.next:
            self.root.next = node
            self.next = node
        else:
            temp = self.root.next  # 获取原来root后面的那个节点
            self.root.next = node  # 将新的节点挂到root上
            node.next = temp # 新的节点的下一个节点是原来的root后的节点
        self.size += 1
    
    def __iter__(self):
        current = self.root.next
        if current:
            while current is not self.next:
                yield current
                current = current.next
            yield current
   
    def find(self,value):
        for n in self.__iter__():
            if n.value == value:
                return n
    
    def find_count(self,value):
        count = 0 
        for n in self.__iter__():
            if n.value == value:
                count += 1
        return count
    def remove(self,value):
        prev = self.root
        for n in self.__iter__():
            # 判断节点的值与要删除的值是否相等
            if n.value == value:
                # 查看是不是最后一个节点
                if n == self.next:
                    # 更新倒数第二节点的关系
                    prev.next = None
                    # 更新最后一个节点为原倒数第二个节点
                    self.next = prev
                prev.next = n.next
                del n
                self.size -= 1
                return True
            prev = n
    def remove_all(self,value):
        prev = self.root
        for n in self.__iter__():
            if n.value == value:
                if n == self.next:
                    prev.next = None
                    self.next = prev
                prev.next = n.next
                del n
                self.size -= 1
                continue
            prev = n

if __name__ == "__main__":
    link = LinkedList()
    link.append('孙悟空')
    link.append('孙悟空')
    link.append('孙悟空')
    link.append('猪八戒')
    link.append('猪八戒')
    link.append('孙悟空')
    link.append('猪八戒')
    link.append('猪八戒')
    link.append('唐僧')
    link.append_first('唐僧')
    link.append_first('唐僧')

    # print(link.find('孙悟空'))
    # print(link.find_count('唐僧'))
    print('-----删除之前------')
    for v in link:
        print(v)
    # link.remove('唐僧')
    # link.remove('唐僧')
    # link.remove('唐僧')
    # link.remove('孙悟空')
    # link.remove('猪八戒')

    # link.remove_all('唐僧')
    # link.remove_all('孙悟空')
    # link.remove_all('猪八戒')
    print('-----删除之后------')
    for v in link:
        print(v)
