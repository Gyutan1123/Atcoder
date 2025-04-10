import sys
import collections, heapq, string, math, itertools, copy, bisect
from sortedcontainers import SortedSet, SortedList, SortedDict
# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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

S = [SI() for _ in range(n)]

T = set()
for _ in range(m):
  t = SI()
  T.add(t)
  
def dfs(tmp,cur,p,l):
  if l > 16:
    return
  
  if cur == n:
    str = ''.join(tmp)
    if 3 <= len(str) <= 16 and not str in T:
      print(str)
      exit()
    else:
      return
    
  if tmp and tmp[-1] != '_':
    if l+1+(n-cur) <= 16:
      dfs(tmp+['_'],cur,p,l+1)
  elif tmp:
    if l+1+(n-cur) <= 16:
      dfs(tmp+['_'],cur,p,l+1)
    
    dfs(tmp+[S[p[cur]]],cur+1,p,l+len(S[p[cur]]))
  else:
    dfs(tmp+[S[p[cur]]],cur+1,p,l+len(S[p[cur]]))

for p in itertools.permutations(range(n)):
  dfs([],0,p,0)
  
print(-1)