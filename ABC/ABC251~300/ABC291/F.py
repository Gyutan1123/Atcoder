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

n,m = MI()

S = [SI() for _ in range(n)]

distFrom1 = [-1]*(n+1)
distFromn = [-1]*(n+1)

que = collections.deque()

que.append(1)
distFrom1[1] = 0 
while que:
  now = que.popleft()
  for j in range(m):
    if S[now-1][j] == '1':
      to = now+j+1
      if distFrom1[to] == -1:
        distFrom1[to] = distFrom1[now]+1
        que.append(to)

que.append(n)
distFromn[n] = 0
while que:
  now = que.popleft()
  for i in range(max(1,now-m)-1,now-1):
    j = now-i-2
    if 0 <= j < m and S[i][j] == '1' and i+j+2 == now and distFromn[i+1] == -1:
      distFromn[i+1] = distFromn[now]+1
      que.append(i+1)
  

ans = []
for k in range(2,n):
  a = float('inf')
  for i in range(max(1,k+1-m), k):
    for j in range(m):
      if (i+j+1 >= k+1 
          and S[i-1][j] == '1' 
          and distFrom1[i] != -1 
          and distFromn[i+j+1] != -1):
        a = min(a, distFrom1[i]+distFromn[i+j+1]+1)
        
  ans.append(a if a < float('inf') else -1)
  
print(*ans)