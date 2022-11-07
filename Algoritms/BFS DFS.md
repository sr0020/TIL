# BFS DFS
---------------------
## BFS
```C
BFS(v)
{
  for(i <- 0; i < n; i <- i+1) do {
    visited[i] <- false;
  }
  
  Q <- createQueue();
  visited[v] <- true;
  v 방문;
  
  while(not isEmpty(Q)) do {
    while(visited[v의 인접 정점 w] = false) do {
      visited[w] <- true;
      w 방문;
      enQueue(Q, w);
    }
    v <- deQueue(Q);
  }
}
```
---------------------
## DFS
```C
DFS(v)
{
  for(i <- 0; i < n; i <- i+1)
  {
    visited[i] <- false;
  }
  stack <- createStack();
  visited[v] <- true;
  
  v 방문;
  
  while(not isEmpty(stack)) do {
    if (visited[v의 인접 정점 w] = false) then {
      push(stack, v);
      visited[w] <- true;
      w 방문;
      v <- w;
    }
    else v <- pop(stack);
  }
}
```
