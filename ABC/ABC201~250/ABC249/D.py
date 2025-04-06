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
A = LI()
dic = collections.defaultdict(int)
for a in A:
    dic[a] += 1
ans = 0
for a in A:
    D = make_divisors(a)
    for d in D:
        if dic[d] > 0:
            if a//d == d:
                ans += dic[d]*dic[d]
            elif dic[a//d] > 0:
                ans += dic[d]*dic[a//d]        
print(ans)    