def MatMul(a,b,mod=None):
  I, J, K = len(a), len(b[0]), len(b)
  c = [[0]*J for _ in range(I)]
  for i in range(I):
    for j in range(J):
      for k in range(K):
        if mod:
          c[i][j] = (c[i][j]+a[i][k]*b[k][j])%mod
        else:
          c[i][j] += a[i][k]*b[k][j]
  
  return c

def MatPow(x,n,mod=None):
  y = [[0]*len(x) for _ in range(len(x))]
  for i in range(len(x)):
    y[i][i] = 1
  while n > 0:
    if n & 1:
      y = MatMul(x,y,mod)
    x = MatMul(x,x,mod)
    n >>= 1
  return y