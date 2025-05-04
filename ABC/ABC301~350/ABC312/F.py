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

P = [LI() for _ in range(n)]

P0 = []
P1 = []
P2 = []

for t,x in P:
  if t == 0:
    P0.append(x)
  elif t == 1:
    P1.append(x)
  else:
    P2.append(x)
    
P0.sort(reverse=True)
P1.sort(reverse=True)
P2.sort(reverse=True)

P0 = P0[:min(len(P0),m)]  
heapq.heapify(P0)


ans = sum(P0)
now = 0
cnt = len(P0)

for x in P2:
  tmp = ans
  if cnt+1 > m and len(P0) > 0:
    tmp -= heapq.heappop(P0) 
  else:
    cnt += 1 

  for i in range(now, min(len(P1), now+x)):
    if cnt+1 > m and len(P0) > 0 and P1[i] > P0[0]:
      tmp -= heapq.heappop(P0)
      tmp += P1[i]
      heapq.heappush(P0, P1[i])
    elif cnt+1 <= m:
      tmp += P1[i]
      heapq.heappush(P0, P1[i])
      cnt += 1
      
  now += x
  
  ans = max(ans, tmp)
  
print(ans)
