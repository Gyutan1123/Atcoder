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
mod = 10**9 + 7
########################################################

n = II()

connect= [[] for _ in range(n+1)]

waza = [LI() for _ in range(n)]

for i in range(n):
  A = waza[i][2:]
  for a in A:
    connect[i+1].append(a)
    
visited = [False]*(n+1)
que = collections.deque()
que.append(n)
visited[n] = True

while que:
  now = que.popleft()
  for to in connect[now]:
    if visited[to] == False:
      visited[to] = True
      que.append(to)

ans = 0
for i in range(n):
  if visited[i+1]:
    ans += waza[i][0]
    
print(ans)