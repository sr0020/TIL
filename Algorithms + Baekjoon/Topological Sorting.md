## Topological Sorting.
#### 1
```C
topologicalSort1(G, v)
{
  for i <- 1 to n
  {
    1. 진입 간선이 없는 정점 u를 선택한다;
      A[i] <- u;
    2. 정점 u와 u의 진출 간선들을 모두 제거한다;
  }
  > 이 시점에 배열 A[1...n]에는 정점들이 위상 정렬되어 있다.
}
```
#### 2
```C
topologicalSort2(G, v)
{
  for each v ∈ V
    visited[v] = NO;
  for each v ∈ V
    if (visited[v] = NO) then DFS_TS(v);
}

DFS-TS(v)
{
  visited[v] = YES;
  for each x ∈ L(v)
    if (visited[v] = NO) then DFS_TS(x);
  1. 연결 리스트 R의 맨 앞에 정점 v를 삽입한다.
}
```
