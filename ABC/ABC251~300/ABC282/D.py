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
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)

colors = [-1]*(n+1)
unvisited = set(range(1,n+1))

colorOffset = 0
while len(unvisited) > 0:
  start = unvisited.pop()
  que = collections.deque()
  que.append(start)
  colors[start] = colorOffset
  unvisited.discard(start)

  while que:
    now = que.popleft()
    nowColor = colors[now]
    for to in connect[now]:
      if colors[to] == nowColor:
        print(0)
        exit()
      if to in unvisited:
        unvisited.discard(to)
        colors[to] = colorOffset+(nowColor+1)%2
        que.append(to)
  
  colorOffset += 2

nums = collections.defaultdict(int)

for i in range(1,n+1):
  nums[colors[i]] += 1    

s = 0
for k in nums.keys():
  s += nums[k]

ans = -m

for k in nums.keys():
  s -= nums[k]
  ans += s*nums[k]
  
print(ans)


