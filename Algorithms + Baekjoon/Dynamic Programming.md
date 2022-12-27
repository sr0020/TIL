- 피보나치 수열
```C
fibo(n)
{
  f[1] <- f[2] <- 1;
  for i <-3 to n
    f[i] <- f[i-1] + f[i-2]
  return f[n]
}
```

- 행렬 경로 문제
```C
matrixPath(n)
{
  for i <- 0 to n
    c[i, 0] <- 0;
  for j <- 1 to n
    c[0, j] <- 0;
  for i <- 1 to n
   for j <- 1 to n
     c[i, j] <- m_ij + max(c[i-1, j], c[i, j-1]);
  return c[n, n]
}
```

- 돌 놓기 문제
```C
pebble(n)
{
  for p <- 1 to 4
    peb[1, p] <- w[1, p];
  for i <- 2 to n
    for p <- 1 to 4
      peb[i, p] <- max{peb[i-1, q]} + w[i, p];
  return max{peb[n, p]};
}
```

- 행렬 곱셈 순서 문제
```C
matrixChain(n)
{
  for i <- to n
    m[i, i] <- 0;
  for r <- 1 to n-r
  {
    j <- i+r;
    m[i, j] <- min{m[i, k] + m[k+1, j] + p_i-1 * p_k * p_j};
  }
  return m[1, n];
}
```

- 최장 공통 부분 순서(LCS)
```C
LCS(m, n)
{
  for i <-0 to m
    C[i, 0] <- 0;
  for j <- 0 to n
    C[0, j] <- 0;
  for i <- 1 to m
    for j <- i to n
      if(x_i = y_i) then C[i, j] <- C[i-1, j-1] + 1;
      else C[i, j] <- max{C[i-1, j], C[i, j-1]};
  retrun C[m, n];
}
```
