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

n = II()
AC = [tuple([tuple(LI()),i]) for i in range(n)]
AC.sort(key=lambda x: (-x[0][0], x[0][1]))

s = SortedSet()
trash = set()
for (a,c),i in AC:
  if len(s) and s[0] < c:
    trash.add(i) 
  s.add(c)

  
ans = []
for i in range(n):
  if i not in trash:
    ans.append(i+1)

print(len(ans))
print(*ans)