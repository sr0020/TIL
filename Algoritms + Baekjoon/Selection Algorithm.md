- 선형 시간 선택 알고리즘
```C
select(A, p, r, i) // i번째 작은 원소를 찾는다.
{
  if (p == r) then return A[p]; // 원소가 하나뿐인 경우
  q <- partition(A, p, r);
  k <- q-p + 1;
  if (i < k) then return select(A, p, q-1, i); // 왼쪽 그룹으로 범위를 좁힘
  else if (i = k) then return A[q]; // i = k
  else return select(A, q+1, r, i-k); // 오른쪽 그룹으로 범위를 좁힘
}
```

- 최악의 선형 시간 선택 알고리즘
```C
linearSelect(A, p, r, i)
{
  1. 원소의 총수가 5개 이하이면 i번째 원소를 찾고 알고리즘을 끝낸다.
  2. 전체 원소를 5개씩의 원소를 가진 [n/5]개의 그룹으로 나눈다.
    (원소의 총수가 5의 배수가 아니면 이 중 한 그룹은 5개 미만이 된다)
  3. 각 그룹에서 중앙값(원소가 5개이면 3번째 원소)를 찾는다.
    이렇게 찾은 중앙값들을 m1, m2, ..., m[n/5]이라 하자
  4. m1, m2, ..., m[n/5]들의 중앙값 M을 재귀적으로 구한다.
    원소의 총수가 홀수이면 중앙값이 하나이므로 문제가 없고
    원소의 총수가 짝수이면 두 중앙값 중 임의로 선택한다. > Call linearSelect()
  5. M을 기준원소로 삼아 전체 원소를 분할한다
    (M보다 작거나 같은 것은 M의 왼쪽에, M보다 큰 것은 M의 오른쪽에 오도록) > Call partition()
  6. 분할된 두 그룹 중 적합한 쪽을 선택해 단계 1~6을 재귀적으로 반복한다. > Call linearSelect()
}
```