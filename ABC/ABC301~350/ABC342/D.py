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

def factorization(n):
  """引数nを素因数分解
     2以上の整数n -> [[素因数, 指数], ...]の2次元リスト
  """
  
  ans = []
  tmp = n
  for i in range(2,int(-(-n**0.5//1))+1):
    if tmp % i == 0:
      cnt = 0
      while tmp % i == 0:
        cnt += 1
        tmp //= i
      ans.append([i,cnt])
      
  if tmp != 1:
    ans.append([tmp,1])
    
  if ans == []:
    ans.append([n,1])
    
  return ans

n = II()
A = LI()


d = collections.defaultdict(int)
zeros = 0
for i in range(n):
  a = A[i]
  if a == 0:
    zeros += 1
    continue
  if a == 1:
    d[()] += 1
    continue
  P = factorization(a)
  tmp = []
  for p,c in P:
    if c%2 == 1:
      tmp.append(p)
  d[tuple(tmp)] += 1

ans = 0
if zeros > 0:
  ans += zeros*(n-zeros)+zeros*(zeros-1)//2


for k in d.keys():
  ans += d[k]*(d[k]-1)//2
print(ans)
