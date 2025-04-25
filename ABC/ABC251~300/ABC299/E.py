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
connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)

k = II()
w = set()
b = [[] for _ in range(k)]

for i in range(k):
  p,d = MI()
  
  que = collections.deque()
  que.append(p)
  
  dist = [-1]*(n+1)
  dist[p] = 0
  
  while que:
    now = que.popleft()
    if dist[now] < d:
      w.add(now)
      for to in connect[now]:
        if dist[to] == -1:
          que.append(to)
          dist[to] = dist[now]+1
      
    elif dist[now] == d:
      b[i].append(now)
    

S = ['0']*(n)

for i in range(k):
  flag = False
  for v in b[i]:
    if not v in w:
      flag = True
      S[v-1] = '1'
    
  if not flag:
    print('No')
    exit()
  
flag = False
for s in S:
  if s == '1':
    flag = True
    
if not flag:
  S[0] = '1'
print('Yes')
print(''.join(S))