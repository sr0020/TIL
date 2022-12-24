# Dijkstra
```C
Dijkstra(G, r)
{
  S <- 0;
  for each u ∈ V
    d[u] <- ∞;  
    d[r] <- 0;
  while (S != V)
  {
    u <- extractMin(V-S, d);
    S <- S∪{u};
    for each v ∈ L(u)
      if (v ∈ V-S and d[u] + w(u, v) < d[v]) then
      {
        d[v] <- d[u] + w(u, v);
        prev[v] <- u;
      }
  }
}

extractMin(Q, d[])
{
  집합 Q에서 d값이 가장 작은 정점 u를 리턴한다.
}
```
------------
# BellmanFord
```C
BellmanFord(G, r)
{
  for each u ∈ V
    d[u] <- ∞;
  d[r] <- 0;
  1. for i <- 1 to |V|-1
    for each (u, v) ∈ E
      if(d[u] + w(u, v) < d[v]) then {
        d[v] <- d[u] + w(u, v);
        prev[v] <- u;
      }
      
   for each (u, v) ∈ E
    if(d[u] + w(u, v) < d[v]) then output "음의 사이클 발견! 해 없음";
}
```
-----------
# FloydWarshall
```C
FloydWarshall(G)
{
  for i <- 1 to n
    for j <- 1 to n
      d_0_ij <- w_ij;
   for k <- to n
    for i <- 1 to n
      for j <- 1 to n
        d_k_ij <- min{d_k-1_ij, d_k-1_ik + d_k-1_kj};
}
```
