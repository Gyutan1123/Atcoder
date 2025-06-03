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

h,w = MI()
A = [LI() for _ in range(h)]
B = [LI() for _ in range(h)]

checked = set()

que = collections.deque()
que.append(A)

checked.add(tuple(map(tuple, A)))

dist = collections.defaultdict(int)

while que:
  nowA = que.popleft()
  if nowA == B:
    print(dist[tuple(map(tuple, nowA))])
    exit()
  for i in range(h-1):
    tmpA = copy.deepcopy(nowA)
    for j in range(w):
      tmpA[i][j], tmpA[i+1][j] = tmpA[i+1][j], tmpA[i][j]
    
    if tuple(map(tuple, tmpA)) not in checked:
      checked.add(tuple(map(tuple, tmpA)))
      que.append(tmpA)
      dist[tuple(map(tuple, tmpA))] = dist[tuple(map(tuple, nowA))] + 1
  
  for i in range(w-1):
    tmpA = copy.deepcopy(nowA)
    for j in range(h):
      tmpA[j][i], tmpA[j][i+1] = tmpA[j][i+1], tmpA[j][i]
    
    if tuple(map(tuple, tmpA)) not in checked:
      checked.add(tuple(map(tuple, tmpA)))
      que.append(tmpA)
      dist[tuple(map(tuple, tmpA))] = dist[tuple(map(tuple, nowA))] + 1

print(-1)