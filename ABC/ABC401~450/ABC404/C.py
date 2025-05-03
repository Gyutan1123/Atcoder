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

n,m = MI()
connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  
  
visited = [False]*(n+1)
finished = [False]*(n+1)
# サイクル検出、復元
# 閉路検出，復元
# https://drken1215.hatenablog.com/entry/2023/05/20/200517
def dfs(now,pre,history):
  visited[now] = True
  history.append(now)
  for to in connect[now]:
    if to == pre:
      continue
    
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

history = []
pos = dfs(1,-1,history)

cycle = reconstruct(pos,history[:-1])
color = [-1]*(n+1)

cycles = set(cycle)

if len(cycles) == n:
  print('Yes')
else:
  print('No')