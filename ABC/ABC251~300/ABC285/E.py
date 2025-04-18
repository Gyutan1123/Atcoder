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
A = LI()

s = [0]
for a in A:
  s.append(s[-1]+a)

dp = [0]*n

for i in range(1,n):
  for j in range(i):
    dp[i] = max(dp[i], dp[j]+dp[i-1-j])
  
  if i % 2 == 0:
    dp[i] = max(dp[i],2*s[i//2])
  else:
    dp[i] = max(dp[i],2*s[i//2]+A[i//2])
    
print(dp[n-1])