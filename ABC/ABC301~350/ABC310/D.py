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

n,t,m = MI()
AB = [LI() for _ in range(m)]
dislike = [[False]*n for _ in range(n)]
for a,b in AB:
  dislike[a-1][b-1] = True
  dislike[b-1][a-1] = True

ans = 0
def dfs(i,j,teams):
  global ans
  if i == n:
    if j == t:
      ans += 1
    return
  
  for k in range(j):
    flag = True
    for l in teams[k]:
      if dislike[i][l]:
        flag = False
        break
    if flag:
      teamsCopy = copy.deepcopy(teams)
      teamsCopy[k].append(i)
      dfs(i+1,j,teamsCopy)

  teamsCopy = copy.deepcopy(teams)
  teamsCopy.append([i])
  dfs(i+1,j+1,teamsCopy)
  
dfs(0,0,[])
print(ans)