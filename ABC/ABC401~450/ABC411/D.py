import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
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

n,q = MI()

d = collections.defaultdict(list)


pcs = [0]*(n+1)

dNum = 1

for i in range(q):
  query = MS()
  if int(query[0]) == 1:
    p = int(query[1])
    pcs[p] = pcs[0]
  if int(query[0]) == 2:
    p = int(query[1])
    s = query[2]

    d[dNum].append(pcs[p])
    d[dNum].append(s)
    pcs[p] = dNum
    dNum += 1
      
  if int(query[0]) == 3:
    p = int(query[1])
    pcs[0] = pcs[p]

ans = []

def dfs(p):
  if p == 0:
    return 
  
  for i in d[p]:
    if isinstance(i, int):
      dfs(i)
    else:
      ans.append(i)
      
dfs(pcs[0])

print(*ans,sep='')