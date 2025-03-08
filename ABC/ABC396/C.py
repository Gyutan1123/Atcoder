n,m = map(int,input().split())
B = list(map(int,input().split()))
W = list(map(int,input().split()))

B.sort()
B.reverse()
W.sort()
W.reverse()

# B_sum[i] : Bの上からi個選んだときの総和
B_sum = [0]
W_sum = [0]

for i in range(n):
    B_sum.append(B_sum[i]+B[i])
for i in range(m):
    W_sum.append(W_sum[i]+W[i])
    
 
W_sum_max =W_sum.index(max(W_sum))  
    
ans = 0


for i in range(n+1):
    B_value_sum = B_sum[i]
    if W_sum_max <= i:
        W_value_sum = W_sum[W_sum_max]
    else:
        W_value_sum = W_sum[i]
        
    ans = max(ans,B_value_sum+W_value_sum)
    
print(ans)

        