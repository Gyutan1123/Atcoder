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

a,b = MS()

dp = [[[0]*4 for _ in range(2)] for _ in range(len(b)+1)]

dp[0][0][0] = 1
for i in range(len(b)):
  for k in range(10):
    if k == 4:
      dp[i+1][1][1] += (dp[i][1][0]+dp[i][1][1])
      dp[i+1][1][3] += (dp[i][1][2]+dp[i][1][3])
    elif k == 9:
      dp[i+1][1][2] += (dp[i][1][0]+dp[i][1][2])
      dp[i+1][1][3] += (dp[i][1][1]+dp[i][1][3])
    else:
      for j in range(4):
        dp[i+1][1][j] += dp[i][1][j]
    
  ni = ord(b[i])-ord('0')
  for k in range(ni):
    if k == 4:
      dp[i+1][1][1] += (dp[i][0][0]+dp[i][0][1])
      dp[i+1][1][3] += (dp[i][0][2]+dp[i][0][3])
    elif k == 9:
      dp[i+1][1][2] += (dp[i][0][0]+dp[i][0][2])
      dp[i+1][1][3] += (dp[i][0][1]+dp[i][0][3])
    else:
      for j in range(4):
        dp[i+1][1][j] += dp[i][0][j]
  
  if ni == 4:
    dp[i+1][0][1] = dp[i][0][0]+dp[i][0][1]
    dp[i+1][0][3] = dp[i][0][2]+dp[i][0][3]
  elif ni == 9:
    dp[i+1][0][2] = dp[i][0][0]+dp[i][0][2]
    dp[i+1][0][3] = dp[i][0][1]+dp[i][0][3]
  else:
    for j in range(4):
      dp[i+1][0][j] = dp[i][0][j]
  

tmp1 = ((dp[len(b)][0][1]+dp[len(b)][1][1])
        +(dp[len(b)][0][2]+dp[len(b)][1][2])
        +(dp[len(b)][0][3]+dp[len(b)][1][3]))

dp = [[[0]*4 for _ in range(2)] for _ in range(len(a)+1)]

dp[0][0][0] = 1
for i in range(len(a)):
  for k in range(10):
    if k == 4:
      dp[i+1][1][1] += (dp[i][1][0]+dp[i][1][1])
      dp[i+1][1][3] += (dp[i][1][2]+dp[i][1][3])
    elif k == 9:
      dp[i+1][1][2] += (dp[i][1][0]+dp[i][1][2])
      dp[i+1][1][3] += (dp[i][1][1]+dp[i][1][3])
    else:
      for j in range(4):
        dp[i+1][1][j] += dp[i][1][j]
    
  ni = ord(a[i])-ord('0')
  for k in range(ni):
    if k == 4:
      dp[i+1][1][1] += (dp[i][0][0]+dp[i][0][1])
      dp[i+1][1][3] += (dp[i][0][2]+dp[i][0][3])
    elif k == 9:
      dp[i+1][1][2] += (dp[i][0][0]+dp[i][0][2])
      dp[i+1][1][3] += (dp[i][0][1]+dp[i][0][3])
    else:
      for j in range(4):
        dp[i+1][1][j] += dp[i][0][j]
  
  if ni == 4:
    dp[i+1][0][1] = dp[i][0][0]+dp[i][0][1]
    dp[i+1][0][3] = dp[i][0][2]+dp[i][0][3]
  elif ni == 9:
    dp[i+1][0][2] = dp[i][0][0]+dp[i][0][2]
    dp[i+1][0][3] = dp[i][0][1]+dp[i][0][3]
  else:
    for j in range(4):
      dp[i+1][0][j] = dp[i][0][j]
      
tmp2 = (dp[len(a)][1][1]+dp[len(a)][1][2]+dp[len(a)][1][3])

print(tmp1-tmp2)