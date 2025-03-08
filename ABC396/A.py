n = int(input())
A = list(map(int,input().split()))

count = 1
for i in range(1,n):
    if A[i] == A[i-1]:
        count += 1
    else:
        count = 1
    
    if count == 3:
        print('Yes')
        exit()
print('No')