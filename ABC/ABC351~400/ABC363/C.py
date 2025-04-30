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
t = set()
ans = 0

if len(set(s)) == len(s):
  print(3628800)
  exit()

for p in set(itertools.permutations(s)):
  flag = True

  tmp = ''.join(p)

  for i in range(n-k+1):
    isPalindrome = True
    for j in range(k):
      if tmp[i+j] != tmp[i+k-1-j]:
        isPalindrome = False
        break
    if isPalindrome:
      flag = False
      break
  
  if flag:
    t.add(tmp)
    
print(len(t))