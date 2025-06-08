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

n = II()

d = collections.defaultdict(list)

ans = [-1]*n
portion = [0]*(n+1)
flag = True
for i in range(n):
  t,x = MI()
  if t == 1:
    d[x].append(i)
    ans[i] = 0
  elif t == 2:
    if d[x]:
      j = d[x].pop()
      ans[j] = 1
      portion[i] -= 1
      portion[j] += 1
    else:
      flag = False
      
if not flag:
  print(-1)
  exit()

for i in range(n):
  portion[i+1] += portion[i]

k = max(portion[:-1])

ans2 = []

print(k)
for a in ans:
  if a != -1:
    ans2.append(a)
print(*ans2)
