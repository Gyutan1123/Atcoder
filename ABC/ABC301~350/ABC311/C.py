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

n = II()
A = LI()
connect = [[] for _ in range(n+1)]
for i in range(n):
  connect[i+1].append(A[i])


visited = [False]*(n+1)
finished = [False]*(n+1)
# サイクル検出、復元
# 閉路検出，復元
# https://drken1215.hatenablog.com/entry/2023/05/20/200517
def dfs(now,pre,history):
  visited[now] = True
  history.append(now)
  for to in connect[now]:
    if finished[to]:
      continue
    
    if visited[to] and not finished[to]:
      history.append(to)
      return to
    
    pos = dfs(to,now,history)
    
    if pos:
      return pos
  
  finished[now] = True
  history.pop()
  return False

def reconstruct(pos,history):
  res = []
  while history:
    v = history.pop()
    res.append(v)
    if v == pos:
      break
  res.reverse()
  return res

for i in range(n+1):
  if finished[i]:
    continue
  history = []
  pos = dfs(1,-1,history)
  cycle = reconstruct(pos,history[:-1])
  if len(cycle) >= 2:
    break
print(len(cycle))
print(*list(cycle))