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

n = II()
if n%2 == 0:
  print(''.join(['-']*((n-1)//2) + ['=='] +['-']*((n-1)//2)))
else:
  print(''.join(['-']*((n-1)//2) + ['='] + ['-']*((n-1)//2)))