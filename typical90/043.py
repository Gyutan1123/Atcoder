import sys
import collections, heapq, string, math, itertools

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

h,w = MI()
rs,cs = MI()
rt,ct = MI()

rs-=1
cs-=1
rt-=1
ct-=1

S = [LS() for _ in range(h)]

# 方向のベクトル
D = [(-1,0),(1,0),(0,-1),(0,1)]

que = collections.deque()
turn = [float('inf')]*(4*h*w)

for i in range(4):
  turn[4*(w*rs+cs)+i] = 0
  que.append(4*(w*rs+cs)+i)

while que:
  now = que.popleft()
  now_turn = turn[now] 
  d = now % 4       # 方向
  r = (now//4) // w # 行
  c = (now//4) % w  # 列
  
  # 方向転換
  for i in range(4):
    to = 4*(r*w+c)+i
    
    if turn[to] > now_turn+1: 
      turn[to] = now_turn+1
      que.append(to)
  
  # 同じ方向への移動
  to_r = r+D[d][0]
  to_c = c+D[d][1]

  if ((0 <= to_r and to_r < h )
      and (0 <= to_c and to_c < w)
      and S[to_r][to_c] == '.'):
    to = 4*(w*to_r+to_c)+d
    if turn[to] > now_turn+1:
      turn[to] = now_turn
      que.append(to)
    
print(min(turn[4*(w*rt+ct):4*(w*rt+ct)+4]))