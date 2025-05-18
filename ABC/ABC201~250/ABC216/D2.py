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

n,m = MI()

places = collections.defaultdict(list)
pipes = []
for i in range(m):
  k = II()
  pipes.append(LI())
  for j in range(k):
    places[pipes[-1][j]].append((i,j))
  pipes[-1].reverse()
  
delCount = [0]*(n+1)

topPairs = collections.deque()

for i in range(1,n+1):
  if [places[i][0][1], places[i][1][1]] == [0,0]:
    topPairs.append((i,places[i][0][0], places[i][1][0]))
  
cnt = 0
while topPairs:
  ball,p1,p2 = topPairs.popleft()
  cnt += 1
  
  pipes[p1].pop()
  pipes[p2].pop()
  
  if len(pipes[p1]) > 0:
    delCount[p1] += 1
    nextBall = pipes[p1][-1]
    if places[nextBall][0][0] == p1:
      places[nextBall][0] = (places[nextBall][0][0], places[nextBall][0][1]-delCount[p1])
    else:
      places[nextBall][1] = (places[nextBall][1][0], places[nextBall][1][1]-delCount[p1])
    
    if places[nextBall][0][1] == 0 and places[nextBall][1][1] == 0:
      topPairs.append((nextBall,places[nextBall][0][0], places[nextBall][1][0]))
  
  if len(pipes[p2]) > 0:
    nextBall = pipes[p2][-1]
    delCount[p2] += 1
    if places[nextBall][0][0] == p2:
      places[nextBall][0] = (places[nextBall][0][0], places[nextBall][0][1]-delCount[p2])
    else:
      places[nextBall][1] = (places[nextBall][1][0], places[nextBall][1][1]-delCount[p2])
    
    if places[nextBall][0][1] == 0 and places[nextBall][1][1] == 0:
      topPairs.append((nextBall, places[nextBall][0][0], places[nextBall][1][0]))
  
if cnt == n:
  print('Yes')
else:
  print('No')