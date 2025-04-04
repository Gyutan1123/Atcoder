import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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
S = SI()

ans = []
que = collections.deque()
que.appendleft(0)

for i in range(n):
  if S[i] == 'L':
    que.appendleft(i+1)
  else:
    ans.append(que.popleft())
    que.appendleft(i+1)

while que:
  ans.append(que.popleft())
  
print(*ans)