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
t = SI()
u = SI()

ascii_lower = string.ascii_lowercase
h = []
for i in range(len(t)):
  if t[i] == "?":
    h.append(i)
  
  
for i in range(26):
  for j in range(26):
    for k in range(26):
      for l in range(26):
        tmp = list(t)
        tmp[h[0]] = ascii_lower[i]
        tmp[h[1]] = ascii_lower[j]
        tmp[h[2]] = ascii_lower[k]
        tmp[h[3]] = ascii_lower[l]
        if u in "".join(tmp):
          print("Yes")
          exit()  
print("No")