import sys
import collections, heapq, string, math, itertools, copy
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

S = [list(SI()) for _ in range(n)]

ans = 'No'

for i in range(n):
  for j in range(n-6+1):
    tmp = 2
    for k in range(6):
      if S[i][j+k] == '.':
        tmp -= 1
    if tmp >= 0:
      ans = 'Yes'
      
for j in range(n):
  for i in range(n-6+1):
    tmp = 2
    for k in range(6):
      if S[i+k][j] == '.':
        tmp -= 1
    if tmp >= 0:
      ans = 'Yes'
      
for i in range(n-6+1):
  for j in range(n-6+1):
    tmp = 2
    for k in range(6):
      if S[i+k][j+k] == '.':
        tmp -= 1
    if tmp >= 0:
      ans = 'Yes'
    
    tmp = 2
    for k in range(6):
      if S[i+k][5+j-k] == '.':
        tmp -= 1
    if tmp >= 0:
      ans = 'Yes'
      
print(ans)