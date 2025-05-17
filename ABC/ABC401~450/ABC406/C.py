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

S = []
for i in range(n-1):
  if P[i] > P[i+1]:
    S.append(-1)
  else:
    S.append(1)
    

from itertools import groupby

def runLengthEncode(S: str):
  grouped = groupby(S)
  res = []
  for k, v in grouped:
      res.append((k, int(len(list(v)))))
  return res

srun = runLengthEncode(S)

ans = 0
for i in range(len(srun)-2):
  if srun[i][0] == 1 and srun[i+1][0] == -1 and srun[i+2][0] == 1:
    ans += srun[i][1] * srun[i+2][1]
  
print(ans)