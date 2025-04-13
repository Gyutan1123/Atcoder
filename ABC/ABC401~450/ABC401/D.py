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

n,k = MI()
s = SI()

if n == 1:
  print('o')
  exit()

res = k
for i in range(n):
  if s[i] == 'o':
    res -= 1

t = list(s)
for i in range(n):
  if t[i] == '?':
    if 0 < i < n-1 and (t[i-1] == 'o' or t[i+1] == 'o'):
      t[i] = '.'
    elif i == 0 and t[i+1] == 'o':
      t[i] = '.'
    elif t == n-1 and t[i-1] == 'o':
      t[i] = '.'
    
qs = []
i = 0
cnt = 0
while i < n:
  if t[i] == '?':
    r = i+1
    while r < n and t[r] == '?':
      r += 1
    if (r-i)%2 == 0:
      cnt += (r-i)//2
    else:
      cnt += (r-i)//2+1
    qs.append((i,r))
    i = r
  else:
    i += 1

if res == 0:
  for i in range(n):
    if t[i] == '?':
      t[i] = '.'
elif res == cnt:
    for q in qs:
      if (q[1]-q[0])% 2 == 1:
        for i in range(q[0],q[1]):
          if (i-q[0]) % 2 == 0:
            t[i] = 'o'
          else:
            t[i] = '.'
            
print(''.join(t))