import sys
import collections, heapq, string

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

# n以下の各整数の、最小の素因数を格納する配列を返す。
def smallest_prime_factors(n):
  spf = [i for i in range(n+1)]
  
  i = 2
  while i**2 <= n:
    if spf[i] == i:
      j = i * 2
      while j <= n:
        if spf[j] == j:
          spf[j] = i
        j += i
    i += 1
  
  return spf

n,k = MI()

spf = smallest_prime_factors(n)

ans = 0

for i in range(2,n+1):
  factors = set()

  while i != 1:
    factors.add(spf[i])
    i = i // spf[i]
    
  if len(factors) >= k:
    ans += 1
  
print(ans)