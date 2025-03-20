"""
ランダムアクセスをO(1)で行えるDeque
https://qiita.com/alumite14/items/e4fb361474eb2bebfbff
"""
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