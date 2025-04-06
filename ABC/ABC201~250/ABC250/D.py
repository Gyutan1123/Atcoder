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
def faster_eratosthenes(n: int):
    """ エラトステネスのふるいによって、n以下の素数を列挙
    
    https://strangerxxx.hateblo.jp/entry/20230227/1677491214

    Args:
        n (int): 正の整数

    Returns: n以下の素数を格納したリスト
        
    """
    if n < 30:
        return [x for x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] if x <= n]
    remains = [1, 7, 11, 13, 17, 19, 23, 29]
    inv_remains = {x: i for i, x in enumerate(remains)}
    msk = 255  # (1 << 8) - 1
    div30 = [i * j // 30 for j in remains for i in remains]
    mod30 = [inv_remains[i * j % 30] for j in remains for i in remains]
    shift = [1 << i for i in range(8)]
    msk8 = [msk - shift[i] for i in range(8)]
    inv_shift = {shift[i]: i for i in range(8)}
    res = [2, 3, 5]
    max_k = n // 30
    import bisect

    max_m = bisect.bisect_right(remains, n % 30) - 1
    sqrtn = int(n**0.5) + 1
    max_sqrt_k = sqrtn // 30
    max_sqrt_m = bisect.bisect_right(remains, sqrtn % 30) - 1
    table = bytearray([msk] * (max_k + 1))
    table[max_k] = (1 << (max_m + 1)) - 1
    table[0] -= 1  # remove 1
    for k in range(max_sqrt_k + 1):
        x = table[k]
        while x:
            u = x & (-x)
            if table[k] & u:
                m = inv_shift[u]
                res.append(k * 30 + remains[m])
                if k == max_sqrt_k and m > max_sqrt_m:
                    break
                # k_before = k
                m_before = m
                i = k * (30 * k + 2 * remains[m]) + div30[(m << 3) + m]
                j = mod30[(m << 3) + m]
                while i < max_k or (i == max_k and j <= max_m):
                    table[i] &= msk8[j]
                    if m_before == 7:
                        i += 2 * k + remains[m] + div30[m << 3] - div30[(m << 3) + 7]
                        j = mod30[m << 3]
                        # k_before += 1
                        m_before = 0
                    else:
                        i += (
                            k * (remains[m_before + 1] - remains[m_before])
                            + div30[(m << 3) + m_before + 1]
                            - div30[(m << 3) + m_before]
                        )
                        j = mod30[(m << 3) + m_before + 1]
                        m_before += 1
            x &= x - 1
    i = table[max_sqrt_k]
    i30 = 30 * max_sqrt_k
    while i:
        j = inv_shift[i & (-i)]
        if i30 + remains[j] > res[-1]:
            res.append(i30 + remains[j])
        i &= i - 1
    i30 += 30
    for i in table[max_sqrt_k + 1 :]:
        while i:
            j = inv_shift[i & (-i)]
            res.append(i30 + remains[j])
            i &= i - 1
        i30 += 30
    return res


n = II()
P = faster_eratosthenes(10**6)

ans = 0

for q in P:
  ans += min(bisect.bisect_right(P,n//(q**3)), bisect.bisect_left(P,q))
  
print(ans)