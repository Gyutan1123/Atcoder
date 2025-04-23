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

def make_divisors(n):
  """ nの約数をO(√n)で列挙する
  https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56

  Args:
      n (int): 正整数

  Returns:
      list: nの約数を格納したリスト
  """
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]


n = II()

ans = 0

for ab in range(1,n):
  cd = n-ab

  ans += len(make_divisors(ab))*len(make_divisors(cd))

print(ans)