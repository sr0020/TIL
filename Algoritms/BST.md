# Binary Search Tree
------------
## Search
```C
treeSearch(t, x)
// t - 트리의 루트 노드
// x - 삽입하고자 하는 키
{
  if(t = NIL or key[t]=x) then {return t};
  if(x < key[t])
    then return treeSearch(left[t], x);
  else return treeSearch(right[t], x);
}
```
------------
## Insertion
```C
treeInsert(t, x)
// t - 트리의 루트 노드
// x - 삽입하고자 하는 키
// 작업 완료 후 루트 노드의 포인터를 리턴한다.
{
  if(t = NIL) then
  {
    key[r] <- x;
    left[r] <- NIL;
    right[r] <- NIL;
    return r;
  }
  if(x < key[t])
    then {left[t] <- treeInsert(left[t], x); return t;}
   else {right[t] <- treeInsert(right[t], x); return t;}
}
```
```C
// 비재귀

treeInsert(t, x)
{
  key[r] <- x;
  left[r] <- NIL;
  right[r] <- NIL;
  
  if(t = NIL) 
    then root <- r;
   else 
   {
      p <- NIL;
      tmp <- r;
      while(tmp != NIL) {
        p <- tmp;
        if(x < key[tmp]) then tmp <- left[tmp];
        else tmp <- right[tmp];
      }
      if(x < key[p]) then left[p] <- r;
       else right[p] <- r;
   }
}
```
-----------
## Deletion
```C
treeDelete(t, r, p)
{
  if(r = t) then root <- deleteNode(t);
  else if(r = left[p])
    then left[p] <- deleteNode(r);
    else right[p] <- deleteNode(r);
}

deleteNode(r)
{
  if(left[r] = right[r] = NIL) then return NIL;
  else if(left[r] = NIL and right[r] != NIL) return right[r];
  else if(left[r] != NIL and right[r] = NIL) return left[r];
  else{
    s <- right[r];
    while(left[s] != NIL)
    {
      parent <-s;
      s <- left[s];
    }
    key[r] <- key[s];
    if(s = right[r])
      then right[r] <- right[s];
      else left[parent] <- right[s];
    return r;
  }
}
```
