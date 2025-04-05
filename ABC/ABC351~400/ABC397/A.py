import sys
import collections, heapq, string

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

x = input()

if int(x[1]) >= 8 or int(x[0]) >= 4:
  print(1)
elif int(x[1]) == 7 and int(x[3]) >= 5:
  print(2)
else:
  print(3)  