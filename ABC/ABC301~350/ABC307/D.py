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
S = SI()

stack = []
discards = []

for i in range(n):
  s = S[i]
  if s == "(":
    stack.append(i)
  elif s == ")":
    if len(stack):
      k = i
      j = stack.pop()
      discards.append((j,k))
    
discards.reverse()
s = set()
for d in discards:
  l,r = d
  if not l in s and not r in s:
    for i in range(l,r+1):
      s.add(i)
      
ans = []
for i in range(n):
  if not i in s:
    ans.append(S[i])
print("".join(ans))