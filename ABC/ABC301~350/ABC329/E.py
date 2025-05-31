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
n,m = MI()
S = list(SI())
T = SI()

que = collections.deque()
for i in range(n-m+1):
  flag = True
  for j in range(m):
    if S[i+j] != T[j]:
      flag = False
      break
  if flag:
    que.append(i)

checked = [False] * n
while que:
  i = que.popleft()
  checked[i] = True
  for j in range(m):
    S[i+j] = '?'
  
  for j in range(max(0, i-m+1), min(n-m+1,i+m)):
    flag = True
    for k in range(m):
      if S[j+k] != T[k] and S[j+k] != '?':
        flag = False
        break
    if flag and not checked[j]:
      que.append(j)

if all(s == '?' for s in S):
  print('Yes')
else:
  print('No')