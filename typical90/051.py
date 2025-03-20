import sys
import collections, heapq, string, math, itertools

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,k,p = MI()
A = LI()

mid = n//2

B = A[:mid]
C = A[mid:]

B_sub_sum = [[] for _ in range(mid+1)]
C_sub_sum = [[] for _ in range(n-mid+1)]

for i in range(mid+1):
  for comb in itertools.combinations(B,i):
    B_sub_sum[i].append(sum(comb))
  B_sub_sum[i].sort()

for i in range(n-mid+1):
  for comb in itertools.combinations(C,i):
    C_sub_sum[i].append(sum(comb))
  C_sub_sum[i].sort()
  
ans = 0 

# Bで選ぶ数
for i in range(mid+1):
  # Cで選ぶ数が多すぎたり負の場合は飛ばす
  if not (0 <= k-i and k-i <= n-mid):
    continue
  for j in range(len(B_sub_sum[i])):
    tmp = B_sub_sum[i][j]
    l = -1
    r = len(C_sub_sum[k-i])
    while r-l > 1:
      m = (r+l)//2
      if C_sub_sum[k-i][m] + tmp > p:
        r = m
      else:
        l = m
    
    ans += r
    
print(ans)