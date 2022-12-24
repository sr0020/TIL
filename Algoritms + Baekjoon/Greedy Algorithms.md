- 최적해가 보장되지 않는 예

1. 이진 트리의 그리디 탐색
```C
Greedy_Sum(T, w[], r)
T: 이진 트리, r: 루트 노트, w[]: 노드들에 할당된 수
{
  x <- r; sum <- 0;
  while(x가 리프 노드가 아님)
  {
    sum <- sum + w[x];
    x <- x의 자식 중 가중치가 큰 자식;
  }
  sum <- sum + w[x];
  return sum;
}
```

2. 보따리 문제
```C
Greedy_knapsack(p[], W[], M)
P[]: 가치 배열, W[]: 부피 배열
X: 보따리에 담는 물건 집합, M: 보따리 부피
{
  P와 W를 P[i]/W[i]에 따라 내림차순(단위 부피 당 가치가 큰 순서)으로 정렬한다.
  headroom <- M; i <- 1;
  while(W[i] <= headroom and i <= n)
  {
    X <- X ∪ {i];
    headroom <- headroom - W[i];
    i++;
  }
  return X;
}
```
---
- 최적해가 보장되는 예

1. 프림 알고리즘
```C
Prim(G, r)
G = (V, E): 주어진 그래프
r: 시작 정점
{
  S <- 0;
  for each u ∈ V
    d[u] <- ∞;
  d[r] <- 0;
  while(S != V)
    u <- extraMin(V-S, d);
    S <- S ∪ {u};
    for each v ∈ L(u)
      if(v ∈ V-S and w(u, v) < d[v]) then 
      {
        d[v] <- w(u, v);
        tree[v] <- u;
      }
}
```

2. 회의실 배정 문제
```C
Greeady_Schedule(S, n)
S= {(s_i, t_i) | i = 1, 2, ..., n}, n: 신청 회의 수
s_i: 시작 시간, t_i: 종료 시간
{
  ti에 대한 오름차순으로 정렬하고, 이 순서대로 S = {(s_i, t_i) | i = 1, 2, ..., n}의 번호를 다시 매긴다;
        => 즉, 종료 시간이 가장 이른 회의가 (s_1, t_1)이 된다
  T <- {1};
  last <- 1;
  for(i <- 2; i <= n; i++)
  {
    if(t_last <= s_i) 
    {
      T <- T ∪ {i};
      last <- i;
    }
  }
  return T;
}
```
---
