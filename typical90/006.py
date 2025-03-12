import sys
import collections, heapq, string

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

n,k = MI()
s = SI()

alphabets = list(string.ascii_lowercase)

# firstAppearIndex[i,j] 
# i番目のアルファベットが、s[j:n]で最初に現れるindex
firstAppearIndex = [[n] * n for _ in range(26)]

for i in range(26):
  if s[n-1] == alphabets[i]:
    firstAppearIndex[i][n-1] = n-1
  for j in reversed(range(n-1)):
    if s[j] == alphabets[i]:
      firstAppearIndex[i][j] = j
    else:
      firstAppearIndex[i][j] = firstAppearIndex[i][j+1]
    
    
ans = ''

tmpHeadIndex = 0
for i in range(k):
  for j in range(26):
    if firstAppearIndex[j][tmpHeadIndex] <= n-k+i:
      tmpHeadIndex = firstAppearIndex[j][tmpHeadIndex] + 1
      ans += alphabets[j]
      break
    
print(ans)