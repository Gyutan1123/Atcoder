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

def nC2(n):
  return n*(n-1)//2

n = II()
A = LI()
d = collections.defaultdict(int)
for a in A:
  d[a] += 1

same = 0
for i in range(1,n+1):
  same += nC2(d[i])

ans = 0
for i in range(n):
  l = i
  r = n-1-i
  if l >= r:
    break

  ans += nC2(r-l+1)-same
  
  # sameを更新
  al = A[l]
  ar = A[r]
  same -= nC2(d[al])  
  d[al] -= 1
  same += nC2(d[al])
  
  same -= nC2(d[ar])
  d[ar] -= 1
  same += nC2(d[ar])

print(ans)