# heapq 模块

import heapq

# heapq中nlargest()与nsmallest()
nums = [1, 43, 4, 12, 34, 43, -2, 4]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


# nlargest()与nsmallest()使用参数key以支持复杂数据结构
portfolio = [
    {'name': 'IBM',  'shares': 100, 'price': 91.1  },
    {'name': 'AAPL', 'shares': 50,  'price': 543.22},
    {'name': 'FB',   'shares': 200, 'price': 21.09 },
    {'name': 'HPQ',  'shares': 35,  'price': 31.75 },
    {'name': 'YHOO', 'shares': 45,  'price': 16.35 },
    {'name': 'ACME', 'shares': 75,  'price': 115.65}
]

cheap = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
expensive =  heapq.nsmallest(3, portfolio, key=lambda s: s['price'])


# heapq模块，堆顶始终为最小元素
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heap[0])
print(heapq.heappop(heap))