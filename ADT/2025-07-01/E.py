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

n,k = MI()
s = SI()

checked = set()
ans = 0
for p in itertools.permutations(range(n)):
  tmp = ''
  for i in range(n):
    tmp += s[p[i]]

  if tmp in checked:
    continue
  
  flag = True
  for j in range(n-k+1):
    f = tmp[j:j+k]
    if f == f[::-1]:
      flag = False
      break
  if flag:
    checked.add(tmp)
    ans += 1
    
print(ans)
