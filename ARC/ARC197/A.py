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

t = II()
for _ in range(t):
  h,w = MI()
  S = SI()
  
  rcnt = 0
  dcnt = 0
  for s in S:
    if s == "D":
      dcnt += 1
    if s == "R":
      rcnt += 1

  wmin = [0]*(h)
  wmax = [0]*(h)
  
  wmax[h-1] = w-1
  
  # ?は基本Dとする場合
  qdcnt = 0
  nowh = 0
  noww = 0
  for i in range(h+w-2):
    s = S[i]
    if s == '?':
      if qdcnt+dcnt+1 <= h-1:
        qdcnt += 1
        nowh += 1
        wmin[nowh] = noww
      else:
        noww += 1
    if s == "D":
      nowh += 1
      wmin[nowh] = noww
    if s == "R":
      noww += 1
    
  # ?は基本Rとする場合
  qrcnt = 0
  nowh = 0
  noww = 0
  for i in range(h+w-2):
    s = S[i]
    if s == '?':
      if qrcnt+rcnt+1 <= w-1:
        qrcnt += 1
        noww += 1
      else:
        wmax[nowh] = noww
        nowh += 1
    if s == "D":
      wmax[nowh] = noww
      nowh += 1
    
    if s == "R":
      noww += 1
        
  ans = 0
  for i in range(h):
    ans += wmax[i]-wmin[i]+1
  
  print(ans)


        