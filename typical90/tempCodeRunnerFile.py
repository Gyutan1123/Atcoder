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
  tmpSum = 0
  cutCount = 0
  preCutPos = 0
  for i in range(n):
    tmpSum += A[i] - preCutPos
    if tmpSum >= mid:
      tmpSum = 0
      cutCount += 1
      
  if l - preCutPos >= mid:
    cutCount += 1
  
  # スコア mid 以上は可能 
  if cutCount >= k:
    left = mid
  else:
    right = mid
    
print(left)
       