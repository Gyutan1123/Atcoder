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
A = LI()
B = LI()

s = set()
connect = [[] for _ in range(n)]
ans = 'Yes'
for i in range(m):
  a,b = A[i], B[i]
  if a == b:
    ans = 'No'
    break
  if a > b:
    a,b = b,a
  if (a,b) in s:
    continue
  s.add((a,b))
  connect[a-1].append(b-1)
  connect[b-1].append(a-1)
  
que = collections.deque()
color = [-1]*n
v = set(range(n))
while v:
  start = v.pop()
  color[start] = 0
  que.append(start)
  while que:
    now = que.popleft()
    nowColor = color[now]
    for to in connect[now]:
      if color[to] == -1:
        color[to] = nowColor^1
        que.append(to)
        v.remove(to)
      elif color[to] == nowColor:
        ans = 'No'
        break
    if ans == 'No':
      break
  
print(ans)