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

S = SI()

if S[0] == '1':
  print('No')
  exit()

row = [[7],[4],[2,8],[1,5],[3,9],[6],[10]]

for i1,i2 in itertools.combinations(range(7),2):
  r1 = row[i1]
  r2 = row[i2]
  if i1 > i2:
    r1, r2 = r2, r1
    i1, i2 = i2, i1
  flag1 = False
  flag2 = False
  for i in r1:
    if S[i-1] == '1':
      flag1 = True
      break
  for i in r2:
    if S[i-1] == '1':
      flag2 = True
      break
  
  if flag1 and flag2:
    for i in range(i1+1, i2):
      r3 = row[i]
      flag = True
      for j in r3:
        if S[j-1] == '1':
          flag = False
          break
      if flag:
        print('Yes')
        exit()
  
print('No') 