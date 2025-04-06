import sys
import collections, heapq, string, math, itertools, copy
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
n,x,y = MI()
A = LI()

B = []

tmp = []
for a in A:
  if y <= a <= x:
    tmp.append(a)
  else:
    if len(tmp) > 0:
      B.append(tmp.copy())
    tmp = []
if len(tmp) > 0:
  B.append(tmp.copy())   
 
ans = 0

for b in B:
  right = 0
  n = len(b)
  s = SortedList()
  
  # 尺取り
  for left in range(n):
    while (right < n and not (x in s and y in s)):
      s.add(b[right])
      right += 1
    
    
    # r = right-1,right,right+1,...,n-1が条件を満たす
    if x in s and y in s:
      ans += n-right+1
    
    if right == left:
      right += 1
    else:
      s.discard(b[left])
    
print(ans)