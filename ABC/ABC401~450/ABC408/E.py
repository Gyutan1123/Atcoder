import sys
import collections
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

connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v,w = MI()
  connect[u].append((v,w))
  connect[v].append((u,w))
  

ans = 0
ban = 0
for i in reversed(range(30)):
  mask = ban | (1 << i)
  
  visited = [False] * (n + 1)
  visited[1] = True
  que = collections.deque([1])
  while que:
    v = que.popleft()
    for u, w in connect[v]:
      if not visited[u] and (w & mask) == 0:
        visited[u] = True
        que.append(u)
  
  if not visited[n]:
    ans |= 1<<i
  else:
    ban |= mask

print(ans)