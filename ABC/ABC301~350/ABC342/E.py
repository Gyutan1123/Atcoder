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
train = [LI() for _ in range(m)]

connect = [[] for _ in range(n)]
for l,d,k,c,a,b in train:
  connect[b-1].append((a-1,l,d,k,c))
  
dp = [-10**20]*n
dp[n-1] = 10**20

visited = [False]*n

pque = [(-10**20,n-1)]

while pque:
  time, now = heapq.heappop(pque)
  time = -time
  
  if visited[now]:
    continue
  
  visited[now] = True
  
  for a,l,d,k,c in connect[now]:
    # 最速でl+cなのでそれがだめなら無理
    if l+c > time:
      continue
      
    j = min(k-1,(time-l-c)//d)
    if dp[a] <= l+j*d:
      dp[a] = l+j*d
      heapq.heappush(pque, (-dp[a],a))
  

for i in range(n-1):
  if dp[i] == -10**20:
    print('Unreachable')
  else:
    print(dp[i])
