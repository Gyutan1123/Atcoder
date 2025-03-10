import sys


II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

n,l = MI()
k = II()
A = LI()
left = 0
right = l

while right - left > 1:
  mid = (right + left) // 2
  
  # 長さがmid以上で最小になるように切る
  pieceCount = 0 
  preCutPos = 0
  for i in range(n):
    if A[i] - preCutPos >= mid:
      pieceCount += 1
      preCutPos = A[i]
      
  if l - preCutPos >= mid:
    pieceCount += 1
    
  # スコア mid 以上は可能 
  if pieceCount >= k+1:
    left = mid
  else:
    right = mid
    
print(left)