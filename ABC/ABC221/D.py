import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n = II()

AB = [LI() for _ in range(n)]

# 座標圧縮
# https://drken1215.hatenablog.com/entry/2021/08/09/235400

C = [0]
for a,b in AB:
  C.append(a)
  C.append(a+b)
  
C = sorted(set(C))
D = { v: i for i, v in enumerate(C)} 

# 逆辞書
iD = dict(zip(D.values(), D.keys()))

count = [0]*len(D)

for a,b in AB:
  count[D[a]] += 1
  count[D[a+b]] -= 1
  
ans = [0]*n
  
for i in range(1,len(D)):
  count[i] += count[i-1]
  
for i in range(1,len(D)-1):
  num = count[i]
  if num > 0:
    ans[num-1] += iD[i+1]-iD[i]

print(*ans)