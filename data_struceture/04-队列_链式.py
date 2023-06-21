
class Node():
    def __init__(self,value=None,prev=None,next=None):
        self.value = value 
        self.prev = prev
        self.next = next
    def __str__(self):
        return 'Node {}'.format(self.value)

class DoubleLinkedList():
    def __init__(self):
        self.root = Node()
        self.size = 0
        self.end = None
    def append(self,value):
        node = Node(value) # 封装节点对象
        # 判断是否已经有数据
        if not self.end:# 如果没有元素
            self.root.next = node # 将root 的下一个节点 设置为新的node节点
            node.prev = self.root # 设置新节点的 上一个节点 为 root
        else:
            self.end.next =node # 将原来最后节点的下一个节点 设置为新的node节点
            node.prev = self.end # 设置新节点的 上一个节点 为 原来的最后一个节点
        self.end = node # 更新最后 一个节点新加的node节点
        self.size += 1 
    def append_first(self,value):
        node = Node(value)
        # 判断是否已经有数据
        if not self.end:# 如果没有元素
            self.end = node # 更新最后 一个节点新加的node节点
        else:
            temp = self.root.next # 保存原来的第一个节点
            node.next = temp # 设置新节的下一个节为原来的 第一个节点
            temp.prev = node # 更新原来的第一个节点的上一个节点位置为 新的node节点
        node.prev = self.root # 设置新节点的 上一个节点 为 root
        self.root.next = node # 将root 的下一个节点 设置为新的node节点
        self.size += 1

    def __iter__(self):
        current = self.root.next
        if current:
            while current is not self.end:
                yield current.value
                current = current.next
            yield current.value
    
    def revers_iter(self):
        current  = self.end #获取最后一节点
        if current:
            while current is not self.root:
                yield current
                current = current.prev
    def remove_first(self):
        if self.end:
            temp =  self.root.next # 获取第一个节点
            self.root.next  = temp.next # 设置第二个节点 root 的下一个节点
            if temp.next: #  判断temp的下一节点是否仍然是一个节点，而不是None
                temp.next.prev = self.root # 设置第一个节点的上一个节点为root
            return temp
class Queue:
    def __init__(self,size =4):
        self.item = DoubleLinkedList()
        self.size = size
        self.length = 0
    def put(self,value):
        self.item.append(value)
        self.length +=1
    def pop(self):
        if self.length <=0:
            return
        self.length -=1
        return self.item.remove_first()

    def empty(self):
        pass

if __name__ == "__main__":
    q = Queue()
    q.put('唐三藏')
    q.put('嫦娥')
    q.put('兔子精')
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    