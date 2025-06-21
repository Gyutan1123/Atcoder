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
n = II()
A = [LI() for _ in range(n)]

pq = set()

d = collections.defaultdict(list)

for i in range(n):
  for a in A[i]:
    d[a].append(i)
    pq.add(a)

pq = list(pq)
heapq.heapify(pq)


F = collections.defaultdict(int)
dp = collections.defaultdict(int)

cnt = [0]*(n)

s = set(range(n))
flag = False

pre = -1
while pq:
  a = heapq.heappop(pq)
  
  if len(s) == 0 and flag:
    tmp = F[pre]
    for i in set(d[a]):
      tmp *= pow(cnt[i],-1,mod)
      tmp %= mod
      
  for i in d[a]:
    if i in s:
      s.remove(i)
    cnt[i] += 1

  if len(s) > 0:
    F[a] = 0
    dp[a] = 0
    pre = a
    continue
  
  elif not flag:
    flag = True
    p = 1
    for i in range(n):
      p *= cnt[i]%mod
      p *= pow(6,-1,mod)
      p %= mod
    F[a] = p
    dp[a] = p
    pre = a
  else:
    for i in set(d[a]):
      tmp *= cnt[i]%mod
      tmp %= mod
    F[a] = tmp
    dp[a] = (tmp - F[pre])%mod
    pre = a 
ans = 0  
for k in dp:
  ans += (dp[k]*k)%mod

ans %= mod
print(ans)