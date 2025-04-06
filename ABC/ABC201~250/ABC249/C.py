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

n,k = MI()
S = [set(SI()) for _ in range(n)]

alphabets = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
for i in range(2**n):
  d = collections.defaultdict(int)
  for j in range(n):
    if (i>>j) & 1:
      for a in S[j]:
        d[a] += 1
  
  tmp = 0
  for a in alphabets:
    if d[a] == k:
      tmp += 1
  
  ans = max(ans,tmp)   

print(ans)