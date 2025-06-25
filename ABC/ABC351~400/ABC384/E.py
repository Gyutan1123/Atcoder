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

h,w,x = MI()
p,q = MI()

S = [LI() for _ in range(h)]

visited = [[False]*w for _ in range(h)]
visited[p-1][q-1] = True
pque = []

if p > 1:
  heapq.heappush(pque, (S[p-2][q-1], p-1, q))
  visited[p-2][q-1] = True
if p < h:
  heapq.heappush(pque, (S[p][q-1], p+1, q))
  visited[p][q-1] = True
if q > 1:
  heapq.heappush(pque, (S[p-1][q-2], p, q-1))
  visited[p-1][q-2] = True
if q < w:
  heapq.heappush(pque, (S[p-1][q], p, q+1))
  visited[p-1][q] = True

ans = S[p-1][q-1]

flag = True

while flag:
  flag = False
  while pque and pque[0][0]*x < ans:
    s,i,j = heapq.heappop(pque)
    flag = True
    ans += s
    if i > 1 and not visited[i-2][j-1]:
      visited[i-2][j-1] = True
      heapq.heappush(pque, (S[i-2][j-1], i-1, j))
    if i < h and not visited[i][j-1]:
      visited[i][j-1] = True
      heapq.heappush(pque, (S[i][j-1], i+1, j))
    if j > 1 and not visited[i-1][j-2]:
      visited[i-1][j-2] = True
      heapq.heappush(pque, (S[i-1][j-2], i, j-1))
    if j < w and not visited[i-1][j]:
      visited[i-1][j] = True
      heapq.heappush(pque, (S[i-1][j], i, j+1))
  
print(ans)
