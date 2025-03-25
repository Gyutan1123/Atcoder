import sys
import collections, heapq, string, math, itertools, copy

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
S = [list(SI()) for _ in range(h)]

que = collections.deque()
que.append((0,0))
punch_num = [[float('inf')]*w for _ in range(h)]
punch_num[0][0] = 0

D = [(1,0),(-1,0),(0,1),(0,-1)]
D_punch = [(1,0),(-1,0),(0,1),(0,-1),
           (1,1),(1,-1),(-1,1),(-1,-1),
           (2,0),(-2,0),(0,2),(0,-2),
           (2,1),(1,2),(-1,2),(-2,1),
           (-2,-1),(-1,-2),(1,-2),(2,-1)]

while que:
  now = que.popleft()
  now_punch_num = punch_num[now[0]][now[1]]
  for d in D:
    toh = now[0]+d[0]
    tow = now[1]+d[1]
    if ((0 <= toh and toh < h ) 
        and (0 <= tow and tow < w)
        ):
      if S[toh][tow] == '.' and punch_num[toh][tow] > now_punch_num:
        punch_num[toh][tow] = now_punch_num
        que.appendleft((toh,tow))
  for d in D_punch:
    toh = now[0]+d[0]
    tow = now[1]+d[1]
    if ((0 <= toh and toh < h ) 
        and (0 <= tow and tow < w)
        ):
      if S[toh][tow] == '#' and punch_num[toh][tow] > now_punch_num+1:
        punch_num[toh][tow] = now_punch_num+1
        que.append((toh,tow))
        
print(punch_num[h-1][w-1])