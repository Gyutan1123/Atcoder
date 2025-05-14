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

d = II()

ans = float("inf")

x = 0
while x*x <= d+1000:
  if x**2 > d:
    y = 0
  else:
    y = int(math.sqrt(d-x**2))
  ans = min(ans, abs(x**2+y**2-d))
  y = y+1
  ans = min(ans, abs(x**2+y**2-d))
  y = y-2
  ans = min(ans, abs(x**2+y**2-d))
  x += 1

print(ans)
