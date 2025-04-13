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


# 永続スタック
# https://qiita.com/wotsushi/items/72e7f8cdd674741ffd61
class PersistentStack:
  def __init__(self, value=None, prev=None):
    self.value = value
    self.prev = prev
  
  def top(self):
    return self.value
  
  def push(self,x):
    return PersistentStack(x, self)
  
  def pop(self):
    return self.prev
  
  
  
note = dict()
q = II()

A = PersistentStack()

ans = []

for _ in range(q):
  query = LS()
  if query[0] == 'ADD':
    A = A.push(query[1])
  
  if query[0] == 'DELETE':
    if A.prev:
      A = A.pop()
    
  if query[0] == 'SAVE':
    note[query[1]] = A
    
  if query[0] == 'LOAD':
    if query[1] in note:
      A = note[query[1]]
    else:
      A = PersistentStack()
  
  if A.top():
    ans.append(A.top())
  else:
    ans.append(-1)
    
print(*ans)