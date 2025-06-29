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

l,r = MI()

sqrt_r = int(r**0.5)+1
isprime = [True]*(sqrt_r+1)
isprime[0] = isprime[1] = False

isprime2 = [True] * (r-l+1)

if l == 1:
  isprime2[0] = False 

for p in range(2,sqrt_r+1):
  if not isprime[p]:
    continue

  q = p*2
  while q <= sqrt_r:
    isprime[q] = False
    q += p
    
  start = l+(-l)%p
  if start == p:
    start += p
  q = start
  while q <= r:
    isprime2[q-l] = False
    q += p
    
P = []
for i in range(len(isprime)):
  if isprime[i]:
    P.append(i)
for i in range(len(isprime2)):
  if isprime2[i]:
    P.append(i+l)

P = set(P)
ans = 1
for p in P:
  q = p
  while q < l+1:
    q *= p
  while q <= r:
    ans += 1
    q *= p

print(ans)
