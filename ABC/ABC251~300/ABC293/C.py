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

h,w = MI()

A = [LI() for _ in range(h)]

visited = [[False]*(w) for _ in range(h)]
ans = 0
def dfs(now, tmp):
  i,j = now
  visited[i][j] = True
  tmp.append(A[i][j])

  if now == (h-1,w-1):
    if len(tmp) == len(set(tmp)):
      global ans
      ans += 1

  if (0 <= i+1 < h 
      and 0 <= j < w 
      and visited[i+1][j] == False):
    tmp2 = tmp.copy()
    dfs((i+1,j),tmp2)

  if (0 <= i < h 
      and 0 <= j+1 < w 
      and visited[i][j+1] == False):
    tmp2 = tmp.copy()
    dfs((i,j+1),tmp2)

  visited[i][j] = False

dfs((0,0), [])

print(ans)
