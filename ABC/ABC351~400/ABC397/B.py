import sys
import collections, heapq, string

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

s = list(SI())
ans = 0
if s[0] == 'o':
  ans += 1

for i in range(len(s)-1):
  if s[i] == 'i' and s[i+1] == 'i':
    ans += 1
  elif s[i] == 'o' and s[i+1] == 'o':
    ans += 1
  
if (len(s) + ans) % 2 == 1:
  ans += 1

print(ans)