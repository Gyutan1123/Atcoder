import sys 
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

l = [list(map(int, input().split())) for _ in range(m)]

G = [[] for _ in range(n)]
for row in l:
    u, v, w = row[0] - 1, row[1] - 1, row[2]
    G[u].append((v, w))
    G[v].append((u, w))
    
    
visited = [False] * n
visited[0] = True

ans = 2**60

def dfs(s,visited,tmp):
  if s == n-1:
    global ans
    ans = min(ans,tmp)
    visited[n-1] = False
    return

  
  for v, w in G[s]:
    if not visited[v]:
      newTmp = w ^ tmp
      visited[v] = True
      dfs(v,visited,newTmp)
    
  visited[s] = False
    
  
  
dfs(0,visited,0)
print(ans)