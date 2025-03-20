import sys
import collections, heapq, string, math, itertools

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

class TwoStackDeque:
    __slots__ = ("front", "back")

    def __init__(self, iterable=None) -> None:
        init_arr = list(iterable) if iterable else []
        mid = len(init_arr) >> 1
        self.front = init_arr[:mid][::-1]
        self.back = init_arr[mid:]

    def _balance(self) -> None:
        source, target = (
            (self.front, self.back) if not self.back else (self.back, self.front)
        )
        mid = len(source) >> 1
        target.extend(source[: mid + 1][::-1])
        del source[: mid + 1]

    def append(self, item) -> None:
        self.back.append(item)

    def appendleft(self, item) -> None:
        self.front.append(item)

    def pop(self):
        if not self:
            raise IndexError("pop from empty deque")
        if not self.back:
            self._balance()
        return self.back.pop()

    def popleft(self):
        if not self:
            raise IndexError("popleft from empty deque")
        if not self.front:
            self._balance()
        return self.front.pop()

    def __getitem__(self, i: int):
        l = len(self)
        if i < -l or l <= i:
            raise IndexError("deque index out of range")
        i = i if i >= 0 else i + l
        if i < len(self.front):
            return self.front[~i]
        else:
            return self.back[i - len(self.front)]

    def __len__(self) -> int:
        return len(self.front) + len(self.back)
      
q = II()
d = TwoStackDeque()
for _ in range(q):
  t,x = MI()
  if t == 1:
    d.appendleft(x)
  if t == 2:
    d.append(x)
  if t == 3:
    print(d[x-1])