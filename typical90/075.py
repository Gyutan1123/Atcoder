import sys
import collections, heapq, string, math, itertools

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
P = factorization(n)
print((sum([p[1] for p in P])-1).bit_length())