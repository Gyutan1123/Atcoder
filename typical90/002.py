import sys


II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

n = II()
ans = []
# bit全探索
for i in range(1 << n):
  tmp = 0
  tmpStr = ''
  flag = True
  for j in range(n):
    # 0101 => ()()
    # 1101 => ))()
    if (i >> ((n-1) - j)) & 1 == 0: 
      # (
      tmp += 1
      tmpStr += '('
    else: 
      # )
      tmp -= 1
      tmpStr += ')'
    
    if tmp < 0:
      flag = False
      break
  
  if flag and tmp == 0:
    ans.append(tmpStr)
    
print('\n'.join(ans))  