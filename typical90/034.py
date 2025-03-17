import sys
import collections, heapq, string, math, itertools
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n,k = MI()
a = LI()
d = collections.defaultdict(lambda:0)    
right = 0
ans = 0
num = 0
for left in range(n):
  while (right < n and (d[a[right]] >= 1 or num < k)):
    if d[a[right]] == 0:
      num += 1
    d[a[right]] += 1 
    right += 1
  ans = max(ans,right-left)
  
  if right == left:
    right += 1
  else:
    d[a[left]] -= 1
    if d[a[left]] == 0:
      num -= 1
      
print(ans)