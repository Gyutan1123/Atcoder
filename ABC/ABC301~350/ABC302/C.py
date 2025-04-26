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
s = [SI() for _ in range(n)]

for p in itertools.permutations(range(n)):
  flag = True
  for i in range(n-1):
    t1 = s[p[i]]
    t2 = s[p[i+1]]
    
    cnt = 0
    for j in range(m):
      if t1[j] != t2[j]:
        cnt += 1
    
    if cnt != 1:
      flag = False

  if flag:
    print('Yes')
    exit()

print('No')