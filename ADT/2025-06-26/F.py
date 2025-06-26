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
S = [SI() for _ in range(n)]

for i in range(n):
  for j in range(n-5):
    cnt = 0
    for k in range(6):
      if S[i][j+k] == '.':
        cnt += 1
    if cnt <= 2:
      print('Yes')
      exit()
  
for j in range(n):
  for i in range(n-5):
    cnt = 0
    for k in range(6):
      if S[i+k][j] == '.':
        cnt += 1
  
    if cnt <= 2:
      print('Yes')
      exit()

for i in range(n-5):
  for j in range(n-5):
    cnt = 0
    for k in range(6):
      if S[i+k][j+k] == '.':
        cnt += 1
    if cnt <= 2:
      print('Yes')
      exit()
      
for i in range(5,n):
  for j in range(n-5):
    cnt = 0
    for k in range(6):
      if S[i-k][j+k] == '.':
        cnt += 1
    if cnt <= 2:
      print('Yes')
      exit()
  
print('No')