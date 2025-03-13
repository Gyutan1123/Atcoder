import sys
import collections, heapq, string

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

Sd = list(SI())
T = list(SI())

ans = []

for i in reversed(range(len(Sd)-len(T)+1)):
  Sd_copy = Sd.copy()
  flag = True 
  for j in range(len(T)):
    if T[j] != Sd[i+j] and Sd[i+j] != '?':
      flag = False
      break

  if flag:
    for j in range(len(T)):
      Sd_copy[i+j] = T[j]
    for j in range(len(Sd)):
      if Sd_copy[j] == '?':
        Sd_copy[j] = 'a'
    ans.append(''.join(Sd_copy))

if ans:
  print(sorted(ans)[0])
else:
  print('UNRESTORABLE')