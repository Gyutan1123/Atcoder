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

n = II()
P = LI()
dp = [[-float('inf')]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

S = [0]
for i in range(n):
  S.append(S[-1]+pow(0.9, i))
 
for i in range(1,n+1):
  for j in range(n+1):
    if i < j:
      break
    
    # 選ぶ場合
    if j == 1:
      dp[i][j] = max(dp[i][j], dp[i-1][j-1]+P[i-1]-1200)
    elif j > 1:
      # 再計算
      
      tmp = dp[i-1][j-1]
      tmp += 1200/math.sqrt(j-1)
      tmp *= S[j-1]
      tmp *= 0.9
      tmp += P[i-1]
      tmp /= S[j]
      tmp -= 1200/math.sqrt(j)
      
      dp[i][j] = max(dp[i][j], tmp)
    
    # 選ばない場合
    dp[i][j] = max(dp[i][j], dp[i-1][j])

print(max(dp[n][1:]))