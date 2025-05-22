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
n = len(S)
ans = []
deque = collections.deque()
nowState = 0
for i in range(n):
  s = S[i]
  if s == 'A':
    deque.append('A')
    nowState = 1
  elif s == 'B':
    if nowState == 1:
      deque.append('B')
      nowState = 2
    else:
      while deque:
        ans.append(deque.popleft())
      ans.append('B')
      nowState = 0
  elif s == 'C':
    if nowState == 2:
      deque.append('C')
      for j in range(3):
        deque.pop()
      if len(deque) == 0:
        nowState = 0
      elif deque[-1] == 'A':
        nowState = 1
      elif deque[-1] == 'B':
        nowState = 2
      
    else:
      while deque:
        ans.append(deque.popleft())
      ans.append('C')
      nowState = 0
  
while deque:
  ans.append(deque.popleft())
print(''.join(ans))