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

n,q = MI()
trains = [[-1,-1] for _ in range(n+1)]

for _ in range(q):
  query = LI()
  if query[0] == 1:
    x,y = query[1:]
    trains[x][1] = y
    trains[y][0] = x
    
  if query[0] == 2:
    x,y = query[1:]
    trains[x][1] = -1
    trains[y][0] = -1
    
  if query[0] == 3:
    x = query[1]
    now = x
    while True:
      if trains[now][0] != -1:
        now = trains[now][0]
      else:
        break
    front = now
    ans = [1,now]
    while True:
      if trains[now][1] != -1:
        now = trains[now][1]
        ans.append(now)
        ans[0] += 1
      else:
        print(*ans)
        break
    
    