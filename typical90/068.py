import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(LS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

# 重みつきUnionFind
# https://at274.hatenablog.com/entry/2018/02/03/140504
class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

n = II()
q = II()

UF = WeightedUnionFind(n+1)

for _ in range(q):
    t,x,y,v = MI()
    if t == 0:
        if x % 2 == 0:
            UF.union(x,y,-v)
        else:
            UF.union(x,y,v)
        print(UF.diff(x,y))

    if t == 1:
        if UF.same(x,y):
            if x % 2 == 0:
                ans = UF.diff(x,y)+v
            else:
                ans = UF.diff(x,y)-v
            if y % 2 == 0:
                print(ans)
            else:
                print(-ans)
        else:
            print('Ambiguous')