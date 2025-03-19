import sys
import collections, heapq, string, math, itertools
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

def dfs(pos, visited, connect):
  tmp = 1
  for to in connect[pos]:
    if visited[to] == False:
      visited[to] = True
      tmp += dfs(to, visited, connect)
  
  d[pos] = tmp
  return tmp

n = II()

# 辺集合
E = []
# 各頂点について、その子要素の数
d = [0]*(n+1)
# 隣接リスト
connect = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)
  E.append((a,b))
          
visited = [False]*(n+1)
visited[1] = True
dfs(1,visited,connect)

ans = 0

for a,b in E:
  # a,b のうちどちらかが子であり、子がaならd[a] < d[b]
  ans += min(d[a],d[b])*(n-min(d[a],d[b]))

print(ans)