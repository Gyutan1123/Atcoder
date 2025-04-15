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

n = II()

s = [SI() for _ in range(n)]

# dp{s}[j][k] = {s}が使用済み、最後がj、いまkの番(k=0:先行,k=1:後攻)
# ここから先行が勝てるかどうか
dp = [[[False]*(2) for _ in range(n)] for _ in range(1<<n)]

for i in reversed(range(1<<n)):
  for j in range(n):
    if (i>>j) & 1 == 0:
      continue
    
    dp[i][j][0] = False   
    dp[i][j][1] = True   
    for select in range(n):
      if (i>>select) & 1 == 1:
        continue
      
      if s[j][-1] == s[select][0]:
        # 1つでも勝てる手があればtrue
        dp[i][j][0] |= dp[i^(1<<select)][select][1]
        # 相手がどうやっても勝てない場合のみtrue
        dp[i][j][1] &= dp[i^(1<<select)][select][0]
  
if n == 1:
  print('First')
else:
  ans = 'Second'
  for i in range(n):
    if dp[1<<i][i][1]:
      ans = 'First'
      
  print(ans)