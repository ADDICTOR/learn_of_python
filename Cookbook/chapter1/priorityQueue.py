# priorityQueue
# 使用heapq模块实现简单的优先级队列

import heapq

class PriorityQueue():

    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __repr__(self) -> str:
        return str(self._queue)


class Item():

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'Item({self.name})'


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())