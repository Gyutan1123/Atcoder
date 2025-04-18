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
n = II()

d = dict()
connect = [[] for _ in range(2*n)]
i = 0
for _ in range(n):
  s,t = MS()
  if s not in d:
    d[s] = i
    i += 1
  if t not in d:
    d[t] = i
    i += 1
  connect[d[s]].append(d[t])
  

visited = [False]*(2*n)
finished = [False]*(2*n)
# サイクル検出
# 閉路検出
# 有向グラフの場合
# https://drken1215.hatenablog.com/entry/2023/05/20/200517
def dfs(now):
  visited[now] = True
  for to in connect[now]:

    if finished[to]:
      continue
    
    if visited[to] and not finished[to]:
      return to
    
    pos = dfs(to)
    
    if pos != -1:
      return pos
  
  finished[now] = True
  return -1

flag = False
for i in range(2*n):
  if dfs(i) != -1:
    flag = True
  
if flag:
  print('No')
else:
  print('Yes')