import sys
import collections, heapq, string, math, itertools, copy

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
A = LI()
A.append(0)

A.sort(reverse=True)


ans = 0

for i in range(n):
  if k == 0:
    break
  
  cnt = (i+1)*(A[i]-A[i+1])
  if k >= cnt:
    k -= cnt
    ans += (i+1)*(A[i]*(A[i]+1) - A[i+1]*(A[i+1]+1))//2
  
  else:
    x = k // (i+1) - 1
    y = k % (i+1)
    
    ans += (i+1)*(A[i]*(A[i]+1) - (A[i]-x-1)*(A[i]-x))//2
    ans += y*(A[i]-x-1)
    break
  
print(ans)