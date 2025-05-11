import sys
import collections, heapq, string, math, itertools, copy, bisect
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################


n,a,b = MI()
D = LI()
D = list(map(lambda x:x%(a+b),D))
D = list(set(D))
D.sort()
D.append(D[0]+a+b) # 最初と最後の要素の比較用


# 間隔がbより大きい区間があれば，そこに平日を設定すればよい
# そうでなければ，平日を設定できない
for i in range(len(D)-1):
  if (D[i+1]-D[i]) > b:
    print('Yes')
    exit()
print('No')