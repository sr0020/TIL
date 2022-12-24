# Analysis of complexity
---------------
#### 알고리즘 분석의 필요성
   + 알고리즘이 자원을 얼마나 소모하는지 분석해야 함.
   + 명확하고, 효율적이어야 함.
--------------
### 시간 복잡도

1. O(1) (한 단계만 처리 함)
``` C
sample(a[], n)
{
   k = n/2; (바닥함수)
   return a[k];
}
```

2. O(n) 
``` C
sample(a[], n)
{
   sum <- 0;
   for i <- 1 to n
      sum <- sum + a[];
   return sum;
}
```

3. O(n^2)
``` C
sample(a[], n)
{
   sum <- 0;
   for i <- 1 to n
      for j <- 1 to n
         sum <- sum + a[i]*a[j];
    return sum;
}
```

4. O(n^3)
``` C
sample(a[], n)
{
   sum <- 0;
   for i <- 1 to n
         for j <- 1 to n {
            k <- a[n]에서 임의로 n/2(정수형)을 뽑을 때 이들 중 최댓값
            sum <- sum + k;
         }
    return sum;
}
```

5. O(n^2)
``` C
sample(a[], n)
{
   sum <- 0;
   for i <- 1 to n-1
      for j <- i+1 to n
         sum <- sum + a[i] * a[j]
    return sum;
}
```

6. O(n)
``` C
factorial(n)
{
   if(n = 1) return 1;
   return n * factorial(n-1);
}
```
-------------
### O 표기법
+ O(g(n)) = {f(n) | 충분히 큰 모든 n에 대하여 f(n) < c(g(n))인 양의 상수 C가 존재한다}
+ O(g(n)) = {f(n) | ∃c > 0, n0 >= 0 s.t. ∀n >= n0, c(g(n)) >= f(n)}

### Ω 표기법
+ Ω(g(n)) = {f(n) | 충분히 큰 모든 n에 대하여 c(g(n)) < f(n) 인 양의 상수 C가 존재한다}
+ Ω(g(n)) = {f(n) | ∃c > 0, n0 >= 0 s.t. ∀n >= n0, c1(g(n)) <= f(n) <= c2(g(n))}

### Θ 표기법
+ Θ(g(n)) = {f(n) | 충분히 큰 모든 n에 대하여 c1(g(n)) < f(n) < c2(g(n))인 양의 상수 C가 존재한다}
+ Θ(g(n)) = {f(n) | ∃c > 0, n0 > 0 s.t. ∀n >= n0, c(g(n)) <= f(n)}
