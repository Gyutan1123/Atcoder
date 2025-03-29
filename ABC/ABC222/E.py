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
mod = 998244353
########################################################

n,m,k = MI()
A = LI()

ecount = [0]*(n-1)
eDict = collections.defaultdict(int)

connect = [[] for _ in range(n+1)]

for i in range(n-1):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  
  eDict[(min(u,v),max(u,v))] = i
  

for i in range(m-1):
  start = A[i]
  goal = A[i+1]
  que = collections.deque()
  que.append(start)
  visited = [False]*(n+1)
  visited[start] = True
  pre = [-1]*(n+1)
  
  while que:
    now = que.popleft()
    for to in connect[now]:
      if visited[to] == False:
        visited[to] = True
        que.append(to)
        pre[to] = now

  now = goal
  while True:
    if now == start:
      break
    to = pre[now]
    ecount[eDict[(min(now,to),max(now,to))]] += 1
    now = to
  
s = sum(ecount)
if s-k < 0 or s%2 != k%2:
  print(0)
  exit()
  
C = max((s+k)//2, (s-k)//2)
dp = [[0]*(C+1) for _ in range(n)]
dp[0][0] = 1
for i in range(n-1):
  for j in range(C+1):
    if j-ecount[i] >= 0:
      dp[i+1][j] = (dp[i][j] + dp[i][j-ecount[i]])%mod
    else:
      dp[i+1][j] = dp[i][j]%mod
      

print(dp[n-1][C]%mod)