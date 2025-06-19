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

n,m,l = MI()
A = LI()
B = LI()
C = LI()

num = A+B+C

# 0:Takahashi, 1:Aoki, 2:ba
dp = [[False,False] for _ in range(3**(n+m+l))]
visited = [[False,False] for _ in range(3**(n+m+l))]
def dfs(now, turn):
  if visited[now][turn]:
    return dp[now][turn]
  visited[now][turn] = True
  # takashiのターン
  if turn == 0:
    flag = False
    for i in range(n+m+l):
      if now//(3**i)%3 == 0:
        next_now = now+2*3**i
        flag = flag | dfs(next_now, 1)
        for j in range(n+m+l):
          if now//(3**j)%3 == 2 and num[i] > num[j]:
            next_now = now+2*3**i-2*3**j
            flag = flag | dfs(next_now, 1)
      
    if flag:
      dp[now][0] = True
    else:
      dp[now][0] = False
    return dp[now][0]
    
  # aokiのターン
  else:
    flag = True
    for i in range(n+m+l):
      if now//(3**i)%3 == 1:
        next_now = now+3**i
        flag = flag & dfs(next_now, 0)
        for j in range(n+m+l):
          if now//(3**j)%3 == 2 and num[i] > num[j]:
            next_now = now+3**i-3**j
            flag = flag & dfs(next_now, 0)
    
    if flag:
      dp[now][1] = True
    else:
      dp[now][1] = False
    
    return dp[now][1]
  
firstState = 0
for i in range(n+m+l):
  if 0 <= i < n:
    continue
  elif n <= i < n+m:
    firstState += 1 * 3**i
  else:
    firstState += 2 * 3**i
    

dfs(firstState, 0)

print("Takahashi" if dp[firstState][0] else "Aoki")
