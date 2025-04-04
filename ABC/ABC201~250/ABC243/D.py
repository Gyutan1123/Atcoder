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

n,x = MI()
S = SI()
stack = []

while x > 0:
  if x & 1:
    stack.append('1')
  else:
    stack.append('0')
  x = x>>1

stack.reverse()

for s in S:
  if s == 'U':
    stack.pop()
  if s == 'L':
    stack.append('0')
  if s == 'R':
    stack.append('1')
   

print(int(''.join(stack),2))