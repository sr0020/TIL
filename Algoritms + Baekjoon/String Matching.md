- Brute Force
```C
naiveMatching(A[], P[])
n: 배열 A[]의 길이, m: 배열 P[]의 길이
{
  for i <- 1 to n-m+1
  {
    if (p[1..m] = A[i ... i+m-1])
      then A[i] 자리에서 매칭이 발견되었음을 알린다.
  }
}
```

- Automata
```C
FA-Matcher(A[], σ[][], F)
F: 목표 상태 집합
{
  n: 배열 A[]의 길이
  q <- 0;
  for i <- 1 to n 
  {
    q <- σ(q, A[i]);
    if (q ∈ F) then A[i-m+1] 자리에서 매칭이 발생했음을 알린다.
  }
}
```

- Rabin-Karp
```C
RadinKarp(A[], P[], d, q)
n: 배열 A[]의 길이, m: 배열 P[]의 길이
{
  p <- 0; b1 <- 0;
  for i <- 1 to m
  {
    p <- (dp + P[i]) mod q;
    b1 <- (db1+ A[i]) mod q;
  }
  h <- d^(m-1) mod q;
  for i <- 1 to n-m+1
  {
    if(i != 1) then b_i <- (d((b_i-1 - hA[i-1]mod q) + A[i+m-1]) mod q;
    if (p = b_i) then
      if(P[1 ... m] = A[i ... i+m-1])
        then A[i] 자리에서 매칭이 되었음을 알린다;
  }
}
```

- KMP
```C
KMP(A[], P[])
n: 배열 A[]의 길이, m: 배열 P[]의 길이
{
  preprocessing(P);
  i <- 1;
  j <- 1;
  
  while(i<=n)
  {
    if(j = 0 or A[i] = P[j])
      then {i++; j++;}
      else j <- pi[j];
    if (j = m+1) then
    {
      A[i-m]에서 매칭되었음을 알린다;
      j <- pi[j]
    }
  }
}

preprocessing(P[])
m: 배열 P[]의 길이 
{
  j <- 1;
  k <- 0;
  pi[1] <- 0;
  while(j <= m)
  {
    if(k = 0 or P[j] = P[k]) then { j++; k++; pi[j] <- k }
    else k <- pi[k];
  }
}
```

- Boyer Moore
```C
BoyerMooreHorspool(A[], P[])
n: 배열 A[]의 길이, m: 배열 P[]의 길이
jump['a']는 기호 'a'에 대한 점프를 의미함
{ 
  computeJump(P, jump);
  i <- 1;
  while (i <= n-m+1)
  {
    j <- m; k <- i+m-1;
    while(j>0 and P[j] = A[k])
    {
      j--; k--;
    }
    if (j = 0) then A[i] 자리에서 매칭이 발견되었음을 알린다;
    i <- i + jump[A[i+m-1];
  }
}
```
