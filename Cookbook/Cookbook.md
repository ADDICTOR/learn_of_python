# Cookbook

## 一：数据结构与算法

### 1.1 将序列分解为单独的变量

- 任何序列（或可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量。唯一的要求是变量的总数和结构要与序列相吻合。

- 如果元素的数量不匹配，将得到一个错误提示：
  
  ```python
  ValueError: need more than  values to unpack
  ```

- *、ign是作为抛弃变量的最好命名！

- ...

### 1.2 从任意长度的可迭代对象中分解元素

- 需要从某个可迭代对象中分解出N个元素，但是这个可迭代对象的长度可能超过N，这会导致出现"分解的值过多（too many values to unpack）"的异常。

- Python的*表达式可用于解决这一问题。对于分解未知或任意长度的可迭代对象，这种扩展的分解操作可谓是量身定做的工具。

- 以下是一些很好的*表达式：
  
  ```python
  # *_
  # *ign
  # *head
  # *tail
  # *fields
  # *args
  # *items
  # *lines
  ```

- 一个巧妙的递归算法：
  
  ```python
  # 递归并非Python强项，因其内在递归限制，所以这个例子请不要在实践中使用
  def sum(items):
      head, *tail = items
      return head + sum(tail) if tail else head
  items = [1, 10, 7, 4, 5, 9]
  sum(items)
  ```

### 1.3 保存最后N个元素

- 保存有限的历史记录可算是collections.deque的完美应用场景了。
- [deque.py](./deque.py)
- 当需要一个简单的队列结构时，collections模块中的deque是不二选择。从队列两端添加或弹出元素的复杂度都是O(1)，这与列表不同，当从头部插入或移除元素时，列表的复杂度为O(N)。

### 1.4 找到最大或最小的N个元素

- heap模块中的nlargest()和nsmallest()
- [heap.py](./heap.py)
- 当所要找的元素数量相对较小时，函数nlargest()和nsmallest()才是最适用的。
- 如果只是简单地想找到最小或最大的元素（N=1时），那么用min()和max()会更加快。
- 如果N和集合本身的大小差不多大，通常更快的方法是先对集合排序，然后做切片操作。

### 1.5 实现优先级队列

- [priorityQueue.py](./priorityQueue.py)

### 1.6 在字典中将键映射到多个值上

- 字典是一种关联容器，每个键都映射到一个单独的值上。如果想让键映射到多个值，需要将这多个值保存到另一个容器如列表或集合中。

- 为了能方便地创建这样的字典，可以利用collections模块中的defaultdict类。defaultdict的一个特点就是它会自动初始化第一个值，这样只需关注添加元素即可。
  
  ```python
  from collections import defaultdict
  
  d = defaultdict(list)
  d['a'].append(1)
  d['a'].append(2)
  d['b'].append(1)
  
  d = defaultdict(set)
  d['a'].add(1)
  d['a'].add(2)
  d['b'].add(1)
  
  # 普通字典的解决方案
  d = {}
  d.setdefault('a', []).append(1)
  d.setdefault('a', []).append(2)
  d.setdefault('b', []).append(4)
  ```

### 1.7 让字典保持有序

- 要控制字典中元素的顺序，可以使用collections模块中的OrderedDict类。当对字典做迭代时，它会严格按照元素初始添加的顺序进行。

- 当想构建一个映射结构以便稍后对其做序列化或编码成另一种格式时，OrderedDict就显得特别有用。
  
  ```python
  import json
  from collections import OrderedDict
  
  d = OrderedDict()
  d['foo'] = 1
  d['bar'] = 2
  d['spam'] = 3
  d['grok'] = 4
  
  # Outputs "foo 1", "bar 2", "spam 3", "grok 4”
  for key in d:
      print(key, d[key])
  print(json.dump(d))
  ```

- OrderedDict内部维护了一个双向链表，它会根据元素加入的顺序来排列键的位置。第一个新加入的元素被放置在链表的末尾。接下来对已存在的键做重新赋值不会改变键的顺序。

- 请注意OrderedDict的大小是普通字典的2倍多，使用时需要认真对应用进行需求分析。

### 1.8 与字典有关的计算问题

- 为了能对字典内容做些有用的计算，通常会利用zip()将字典的键和值反转过来。
  
  ```python
  prices = {
  'ACME': 45.23,
  'AAPL': 612.78,
  'IBM': 205.55,
  'HPQ': 37.20,
  'FB': 10.75
  }
  min_price = min(zip(prices.values(), prices.keys()))
  max_price = max(zip(prices.values(), prices.keys()))
  prices_sorted = sorted(zip(prices.values(), prices.keys()))
  ```

- zip()创建的为迭代器，内容仅能消费一次。

### 1.9 在两个字典中寻找相同点

- 关于字典的键有一个很少有人知道的特性，那就是它们也支持常见的集合操作，比如求并集、交集和差集。

- 字典的items()方法返回由(key,value)对组成的items-view对象。这个对象支持类似的集合操作，可用来完成找出两个字典间有哪些键值对有相同之处的操作。
  
  ```python
  # & - | 代表集合运算中的交并补
  ```

### 1.10 从序列中移除重复项且保持元素间顺序不变

- 当一个序列中的值是可哈希的，可以通过集合和生成器轻易实现对序列的去重排序。
  
  ```python
  def dedupe(items, key=None):
      seen = set()
      for item in items:
          val = item if key is None else key(item)
          if val not in seen:
              yield item
              seen.add(val)
  
   nums = [1, 34, 43, 43, 65, 656, 1]
   nums = list(dedupe(nums))
  ```

- 如果希望在一个较复杂的数据结构中，只根据对象的某个字段或属性来去除重复项，这种解决方案同样能完美工作。

### 1.11 对切片命名

- 这里我们介绍一种切片对象slice(start, stop, step)。
- 通过对切片命名可以提高代码复用性与可读性。

### 1.12 找出序列中出现次数最多的元素

- collections模块中的Counter类可以很好的解决这一问题，most_common()方法可以直接告诉我们答案。
- Counter是一个对原序列进行计数统计后生成的字典Counter({})。
- Counter类支持自增、update()、以及数学运算操作。

### 1.13 通过公共键对字典列表排序

- operator模块中的itemgetter函数可以很好解决这一问题。

- 以下两种方案是等价的：
  
  ```python
  from operator import itemgetter
  rows = [{"name":1},{"name":2},{"name":3}]
  rows_by_name = sorted(rows, key=itemgetter("name"))
  rows_by_name = sorted(rows, key=lambda s: s["name"])
  ```

- rows被传递给内建的sorted()函数，该函数接受一个关键字参数key。这个参数应该代表一个可调用对象（callable），该对象从rows中接受一个单独的元素作为输入并返回一个用来做排序依据的值。itemgetter()函数创建的就是这样一个可调用对象。

- itemgetter方法同样适用于min()与max()。

- Tips：itemgetter方法比匿名函数性能更好。

### 1.14 对不原生支持比较操作的对象排序

- 显然地，sorted()+lambda函数的方案可以很好的实现。
- 这里我们介绍operator.attrgetter()，和itemgetter于字典一样，attrgetter()方法是一种获取对象属性作为可调用对象（callable）的方案。
- attrgetter与itemgetter同样支持多属性/多键值。

### 1.15 根据字段将记录分组

- 这里我们介绍itertools中的grouby()函数。
  
  ```python
  from operator import itemgetter
  from itertools import groupby
  
  # Sorted by the desired field first
  rows.sort(key=itemgetter('date'))
  
  # Iterate in groups
  for date, items in groupby(rows, key=itemgetter('date')):
      print(date)
      for i in items:
          print(" ", i)
  ```

- 函数groupby()通过扫描序列找出拥有相同值（或是由参数key指定的函数所返回的值）的序列项，并将它们分组。

- groupby()创建了一个迭代器，而在每次迭代时都会返回一个值（value）和一个子迭代器（sub_iterator），这个子迭代器可以产生所有在该分组内具有该值的项。

- 首先要根据感兴趣的字段对数据进行排序。因为groupby()只能检查连续的项。

- 如果只是简单地根据日期将数据分组到一起，放进一个大的数据结构中以允许进行随机访问，那么利用defaultdict()构建一个一键多值字典（multidict）可能会更好,因为此刻我们无需排序。例如：
  
  ```python
  from collections import defaultdict
  rows_by_date = defaultdict(list)
  for row in rows:
      rows_by_date[row["date"]].append(row)
  ```

### 1.16 筛选序列中的元素

- 列表推导式（list comprehension）。

- 生成器表达式。

- 内建filter(func, values)，该方法创建一个迭代器。

- 另一个值得一提的筛选工具是itertools.compress(iter,selector)，它接受一个可迭代对象以及一个布尔选择器序列作为输入。输出时，它会给出所有在相应的布尔选择器中为True的可迭代对象元素。如果想把对一个序列的筛选结果施加到另一个相关的序列上时，这就会非常有用。

- 同样地，compress方法生成一个迭代器。

### 1.17 从字典中提取子集

- 字典推导式（dictionary comprehension）。
- 大部分可以用字典推导式解决的问题也可以通过创建元组序列然后将其传给dict()函数完成。
- 但字典表达式更为清晰与高效。

### 1.18 将名称映射到序列的元素中

- 相比普通的元组，collections.namedtuple()（命名元组）只增加了极小的开销就提供了这些便利。实际上collections.namedtuple()是一个工厂方法，它返回的是Python中标准元组类型的子类。
  
  ```python
  from collections import namedtuple
  Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
  sub = Subscriber('Beijing', '2023-06-08')
  ```

- namedtuple的一种可能用法是作为字典的替代，后者需要更多的空间来存储。因此，如果要构建涉及字典的大型数据结构，使用namedtuple会更加高效。但是请注意，与字典不同的是，namedtuple是不可变的（immutable）。

- namedtuple实例的_replace()方法以创建一个新实例并替换掉原有实例的方式修改属性值。

- 如果目标是定义一个高效的数据结构，而且将来会修改各种实例属性，那么使用namedtuple并不是最佳选择。

### 1.19 同时对数据做转换和换算

- 结合换算函数（reduction）与生成器表达式

### 1.20 将多个映射合并为单个映射

- 一种简单的方案是利用collections模块中的ChainMap类来解决这一问题，ChainMap可接受多个映射然后再逻辑上使它们表现为一个单独的映射结构。

- 然而，这些映射在字面上并不会合并在一起。相反，ChainMap只是简单地维护一个记录底层映射关系的列表，然后重定义常见的字典操作来扫描这个列表。

- 作为ChainMap的替代方案，我们可能会考虑利用字典的update()方法将多个字典合并在一起。但这需要单独构建一个完整的字典对象（或者修改其中现有的一个字典，这就破坏了原始数据）。此外，如果其中任何一个原始字典做了修改，这个改变都不会反应到合并后的字典中。

## 二：迭代器与生成器

### 2.1 手动访问迭代器中的元素

- 特殊情况下需要手动访问可迭代对象中的元素时，可以使用next()函数，通过try-except捕获StopIteration异常

  ```python
  with open('/etc/passwd') as f:
      try:
          while True:
            line = next(f)
            prtin(line, end='')
      except StopIteration:
          pass
  ```

  ```python
  with open('/etc/passwd') as f:
      while True:
          line = next(line, None)
          if not line:
              break
          print(line, end='')
  ```

### 2.2 委托迭代

- 当构建自定义容器对象时，若其内部持有列表、元组或其他可迭代对象，我们可以通过委托迭代的方式使新容器能自行完成迭代操作。

- 通常来说，我们只需定义一个__iter__()方法，将迭代请求委托到对象内部持有的容器。

  ```python
  class Node():
      def __init__(self, value):
          self._value = value
          self._children = []

      def __iter__(self):
          return iter(self._children)

  root = Node(0)
  for ch in root:
      print(ch)
  ```

- 上述示例中使用iter()函数通过调用s.__iter__()来简单地返回底层的迭代器，这和len(s)调用s.__len__()的方式是一样的。

### 2.3 用生成器创建新的迭代方式

- 可以使用生成器函数定义一种新的迭代模式，使其区别于常见的内建函数。

  ```python
  def frange(start, stop, increment):
      x = start
      while x < stop:
          yield x
          x += increment
  ```

- 我们可以通过for循环对上述函数frange()的实例进行迭代，也可以通过sum()、list()等函数来访问迭代对象中的元素。

- 函数中只要出现了yield语句就会使其转变为一个生成器，与普通函数不同的是，生成器只有在响应迭代操作时才会运行。

### 2.4 实现迭代协议

- 使用生成器函数，可以使我们的自定义对象支持迭代操作，同时以简单的方式实现迭代协议。

- [iteration.py](./iteration.py)

- Python的迭代协议要求__iter__()返回一个特殊的迭代器对象，该对象必须实现__next__()方法，并使用StopIteration异常来通知迭代的完成。

- DepthFirstIterator类的工作方式和生成器版本的实现相同但是更复杂，因为迭代器必须维护迭代过程中许多复杂的状态，要标记当前迭代过程的位置。

### 2.5 反向迭代

- 可以使用内建函数reversed()函数实现反向迭代。

- 反向迭代只有在待处理的对象拥有可确定的大小，或者对象实现了__reversed__()特殊方法时，才能奏效。如果两个条件都无法满足，必须首先将这个对象转换为列表（这种行为通常需要消耗大量内存）。

- 当我们实现了__reversed__()方法，可以在自定义的类上实现反向迭代。

  ```python
  class Countdown:
      def __init__(self, start):
          self.start = start
      # Forward iterator
      def __iter__(self):
          n = self.start
          while n > 0:
              yield n
              n -= 1

      # Reverse iterator
      def __reversed__(self):
          n = 1
          while n <= self.start:
              yield n
              n += 1
  ```

### 2.6 定义带有额外状态的生成器函数

- 以类的方式实现生成器，将生成器函数的代码放到__iter__()方法中。