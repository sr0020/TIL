- 충돌 해결법

1. 체이닝
```C
chainedHashInsert(T[], x)
T: 해시 테이블, x: 삽입 원소
{
  리스트 T[h(x)]의 맨 앞에 x를 삽입;
}

chainedHashSearch(T[], x)
T: 해시 테이블, x: 검색 원소
{
  리스트 T[h(x)]에서 x값을 가지는 원소를 검색;
}

chainedHashDelete(T[], x)
T: 해시 테이블, x: 삭제 원소
{
  리스트 T[h(x)]에서 x의 노드를 삭제
}
```
---
2. 개방 주소 방법
```C
hashInsert(T[], x)
{
  i <- 0;
  repeat {
    j <- h_i(x);
    if (T[j] = NIL)
      then {T[j] <- x; return j;}
      else i++;
  } until (i = m)
  error "테이블 오버플로"
}

hashSearch(T[], x)
{
  i <- 0;
  repeat {
    j <- h_i(x);
    if (T[j] = x)
      then return j;
      else i++;
  } until (T[j] = NIL or i = m)
  return NIL;
}
```
