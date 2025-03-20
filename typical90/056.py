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

n,s = MI()

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True
buy= [['']*(s+1) for _ in range(n+1)]
for i in range(n):
  a,b = MI()
  for j in range(s+1):
    if 0 <= j-a and j-a <= s and dp[i][j-a]:
      dp[i+1][j] = True
      buy[i+1][j] = ('A',a)
      
    if 0 <= j-b and j-b <= s and dp[i][j-b]:
      dp[i+1][j] = True
      buy[i+1][j] = ('B',b)
    
if dp[n][s] == False:
  print('Impossible')
else:
  ans = []
  tmp = s
  for i in reversed(range(1,n+1)):
    ans.append(buy[i][tmp][0])
    tmp -= buy[i][tmp][1]
  
  print(''.join(reversed(ans)))