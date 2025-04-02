import sys
import collections, heapq

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

q = II()

que = collections.deque()
heap = []
heapq.heapify(heap)

for i in range(q):
  query = LI()

  if query[0] == 1:
    x = query[1]
    que.append(x)
    
  elif query[0] == 2:
    if len(heap) > 0:
      print(heapq.heappop(heap))
    else:
      print(que.popleft())
      
  else:
    while que:
      heapq.heappush(heap,que.popleft())