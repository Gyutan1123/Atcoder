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

n,k = MI()

studentNum = [[0]*5001 for _ in range(5001)] 

for i in range(n):
  a,b = MI()
  studentNum[a][b] += 1
  
for x in range(5001):
  for y in range(5000):
    studentNum[x][y+1] += studentNum[x][y]
    
for y in range(5001):
  for x in range(5000):
    studentNum[x+1][y] += studentNum[x][y]
  
ans = 0

for x in range(5001):
  for y in range(5001):
    tmp = studentNum[x][y]
    if x-k-1 >= 0 and y-k-1 >= 0:
      tmp -= studentNum[x-k-1][y] + studentNum[x][y-k-1] - studentNum[x-k-1][y-k-1]
    elif x-k-1 >= 0:
      tmp -= studentNum[x-k-1][y]
    elif y-k-1 >= 0:
      tmp -= studentNum[x][y-k-1]
    ans = max(ans,tmp)
    
print(ans)