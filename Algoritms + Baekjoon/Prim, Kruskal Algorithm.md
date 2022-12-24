## 프림 알고리즘
```C
Prim(G, r)
{
  S <- 0;
  for each u ∈ V
    d[u] <- ∞;
    d[r] <- 0;
    while (S != V)
    {
      u <- extractMin(V-S, d);
      S <- S ∪ {u};
      for each v ∈ L(u)
        if(v ∈ V-S and w(u, v) < d[v]) then
        {
          d[v] <- w(u, v);
          tree[v] <- u;
        }
    }
}

extractMin(Q, d[])
{
  집합 Q에서 d값이 가장 작은 정점 u를 리턴한다;
}
```
-------------
## 크루스칼 알고리즘
```C
Kruskal(G)
{
  T <- 0;
  1. 단 하나의 정점만으로 구성된 n개의 집합을 초기화한다.
  2. 모든 간선을 가중치의 크기 순으로 정렬하여 배열 A[1...E]에 저장한다;
  3. while (T의 간선 수 < n-1)
    {
      4. A에서 최소 비용의 간선 (u, v)를 제거한다.
      5. if(정점 u와 v가 다른 집합에 속함) then {
        6. T <- T ⊂ {(u, v)};
        7. 정점 u와 v가 속한 두 집합을 하나로 합친다;
      }
    }
}
```
