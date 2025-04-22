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

IN = [0]*(n+1)

connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  IN[v] += 1

# Kahnのアルゴリズムでトポロジカルソートする

que = collections.deque()

for i in range(1,n+1):
  if IN[i] == 0:
    que.append(i)
    
flag = True
result = []
while que:
  if len(que) >= 2:
    flag = False
  now = que.popleft()
  result.append(now)
  for to in connect[now]:
    IN[to] -= 1
    if IN[to] == 0:
      que.append(to)
      
if flag:
  print('Yes')
  ans = [-1]*(n)
  for i,j in enumerate(result):
    ans[j-1] = i+1
  print(*ans)
else:
  print('No')