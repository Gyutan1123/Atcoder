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

n,m = MI()
S = LI()
X = LI()

d = collections.defaultdict(int)

B = [0]

for i in range(n-1):
  B.append(-B[-1]+S[i])


for i in range(n):
  for j in range(m):
    d[(B[i]-X[j])*(-1)**(i+1)] += 1
print(max(d.values()))