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

n = II()

s = [0]*(2*10**5+1)

for _ in range(n):
  l,r = MI()
  s[l] += 1
  s[r] -= 1

for i in range(1,2*10**5+1):
  s[i] += s[i-1]


ans = []

now = 1
flag = False

while now < 2*10**5+1:
  if s[now] == 0:
    now += 1
    continue
  else:
    flag = True
    l = now
    r = now+1
    
    while r < 2*10**5+1 and s[r] > 0:
      r += 1
    now = r+1
    ans.append((l,r))


for a in ans:
  print(*a)