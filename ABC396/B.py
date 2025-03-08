q = int(input())

yama = [0]*100

for i in range(q):
  query = list(map(int,input().split()))
  if (query[0]) == 1:
    yama.append(query[1])
  
  else:
    print(yama.pop())