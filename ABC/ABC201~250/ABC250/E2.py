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

# E Zobrist Hashによる別解
import random

n = II()
A = LI()
B = LI()
q = II()

table = {}
for a in A:
  table[a] = random.randrange(1 << 60)
for b in B:
  table[b] = random.randrange(1 << 60)
  
hashA = [0]
setA = set()
for a in A:
  if a in setA:
    hashA.append(hashA[-1])
  else:
    setA.add(a)
    hashA.append(hashA[-1]^table[a])

hashB = [0]
setB = set()
for b in B:
  if b in setB:
    hashB.append(hashB[-1])
  else:
    setB.add(b)
    hashB.append(hashB[-1]^table[b])
    
    
for i in range(q):
  x,y = MI()
  print('Yes' if hashA[x] == hashB[y] else 'No')