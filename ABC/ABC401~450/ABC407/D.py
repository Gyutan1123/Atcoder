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
h,w = MI()
A = [LI() for _ in range(h)]
memo = set()
def check(res):
  global memo
  tmp = tuple(res)
  if tmp in memo:
    return False 
  else:
    memo.add(tmp)
    return True
def calc(res):
  global ans
  tmpans = 0
  for i,j in res:
    tmpans = tmpans^A[i][j]
  ans = max(ans, tmpans)  

ans = -float('inf')
def dfs(res):
  calc(res)
  if len(res) == 0:
    return
  
  for i,j in res:
    if (i+1,j) in res:
      tmp = res.copy()
      tmp.remove((i,j))
      tmp.remove((i+1,j))
      if check(tmp):
        dfs(tmp)
    if (i,j+1) in res:
      tmp = res.copy()
      tmp.remove((i,j))
      tmp.remove((i,j+1))
      if check(tmp):
        dfs(tmp)
        
res = set()
for i in range(h):
  for j in range(w):
    res.add((i,j))

dfs(res)
print(ans)