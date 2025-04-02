import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')


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
A = [LI() for _ in range(2*n-1)]
ans = -1 

used = [False]*(2*n)

def makeGroup(tmp):
  if all(used):
    global ans
    ans = max(ans,tmp)
    return

  for i in range(2*n):
    if not used[i]:
      used[i] = True
      break

  for j in range(i+1,2*n):
    if not used[j]:
      used[j] = True
      makeGroup(tmp^A[i][j-i-1])
      used[j] = False

  used[i] = False

makeGroup(0)
print(ans)