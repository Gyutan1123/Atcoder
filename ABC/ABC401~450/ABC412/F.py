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
mod = 998244353
########################################################

n,c = MI()
A = LI()
A[c-1] += 1
cnum = A[c-1]
A.sort()



S = [0]
for a in A:
  S.append((S[-1]+a))
  
A.insert(0, 0)  
  
dp = [0]*(n+1)
tmp = 0
for i in range(n,0,-1):
  dp[i] = ((S[n]-1+tmp)%mod)*pow((S[n]-1-S[i-1]),-1,mod)%mod
  tmp += A[i]*dp[i]%mod
  

for i in range(1,n+1):
  if A[i] == cnum:
    ans = dp[i]
    break
print(ans%mod)
