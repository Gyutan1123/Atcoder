import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n = II()

# scoreSum[i][j] = i+1組の学籍番号j番までの学生の期末試験点数の合計
scoreSum = [[0]*(n+1) for _ in range(2)]

for i in range(1,n+1):
  c,p = MI()
  scoreSum[c-1][i] = p
  
for i in range(2):
  for j in range(n):
    scoreSum[i][j+1] += scoreSum[i][j]
    
q = II()
for _ in range(q):
  l,r = MI()
  print(scoreSum[0][r] - scoreSum[0][l-1],scoreSum[1][r] - scoreSum[1][l-1])
