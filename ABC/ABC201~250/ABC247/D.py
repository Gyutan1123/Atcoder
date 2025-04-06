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



q = II()

que = collections.deque()

for _ in range(q):
  query = LI()
  if query[0] == 1:
    que.append(query[1:])
  
  if query[0] == 2:
    c = query[1]
    
    tmp = 0
    ans = 0
    
    while True:
      X,C = que.popleft()
      tmp += C
      ans += C*X
      if tmp > c:
        ans -= (tmp-c)*X
        que.appendleft((X,tmp-c))
        break
      if tmp == c:
        break
      
    print(ans)