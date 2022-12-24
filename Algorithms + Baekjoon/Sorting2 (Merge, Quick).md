# Sorting2 (Merge, Quick Sort)
---------------
## Merge Sort
+ 수도 코드
```C
mergeSort(A[], p, r)
{
  if(p < r) then
  {
    q <- (p+r) / 2;
    mergeSort(A, p, q);
    mergeSort(A, q+1, r);
    merge(A, p, q, r);
  }
}

Merge(A[], p, q, r)
{
  merge two sorted arrays A[p ~ q] and A[q+1 ~ r]
  create a sorted array A[p ~ r]
}
```
```C
Merge(A[], p, q, r)
{
  i <- p; j <- q+1; t <-1;
  while(i <= q and j <= r)
  {
    if(a[i] < a[j])
      then temp[t++] = a[i++]
    else temp[t++] = a[j++]
  }
  while(i <= q)
    temp[t++] = a[i++]
  while(j <= r)
    temp[t++] = a[j++]
    
  i <- p; t <- 1;
  
  while(i <= r)
    a[i++] = temp[t++]
}
```
+ 코드
```C
#include <stdio.h>
int size = 5;
int temp[5] = { 0, };

void merge(int a[], int p, int q, int r)
{
	int i = p; // left
	int j = q + 1; // mid+1
	int t = p; // left

	// 분할 정렬된 list의 합병
	while (i <= q && j <= r)
	{
		if (a[i] < a[j])
		{
			temp[t++] = a[i++];
		}
		else temp[t++] = a[j++];
	}

	// 수도코드와 다른 부분
	// 남아있는 값들 일괄 복사
	if (i > q)
		for (int k = j; k <= r; k++)
			temp[t++] = a[k];
	else
		for (int k = i; k <= q; k++)
			temp[t++] = a[k];

	// 수도코드와 다른 부분
	// 임시 배열의 리스트를 배열 a[]로 재복사
	for (int k = p; k <= r; k++)
		a[k] = temp[k];
}

void mergeSort(int a[], int p, int r) 
{
	if (p < r)
	{
		int q = (p + r) / 2;
		mergeSort(a, p, q);
		mergeSort(a, q + 1, r);
		merge(a, p, q, r);
	}
}

int main(void)
{
	int list[5] = { 3, 4, 2, 5, 1 };

	// 합병 정렬 수행 (left: 배열의 시작 = 0, right: 배열의 끝 = 7
	mergeSort(list, 0, size-1); 

	for (int i = 0; i < size; i++)
	{
		printf("%d\n", list[i]);
	}

	return 0;
}

```
--------------
## Quick Sort
+ 수도 코드
```C
quickSort(A[], p, r)
{
  if(p < r) then
    q = partition(A, p, r);
    quickSort(A, p, q-1);
    quickSort(A, q+1, r);
}
partition(A[], p, r)
{
  relocates the elements of array A[p~r] on both
  sides of A[r] and returns the position of A[r];
}
```
```C
partition(A[], p, r)
{
   pivot = (p + r) / 2;
   left <- p;
   right <- r;
   
   while(left < right) do
   {
   	while(A[left] < A[pivot] and left < right) do left++;
	while(A[right] >= A[pivot] and left < right) do right--;
	if(left < right) then
	{
	     temp <- A[left];
	     A[left] <- A[right];
	     A[right] <- temp;
	}
   }
   temp <- A[pivot];
   A[pivot] <- A[right];
   A[right] <- templ
   return right;
}
```
+ 코드
```C
#include <stdio.h>
int size = 5;
int temp;

int partition(int a[], int p, int r)
{
	int pivot = ((int)(p + r) / 2);
	int left = p;
	int right = r;

	while (left < right)
	{
		// left가 피벗보다 작으면 계속 left를 증가
		while ((a[left] < a[pivot]) && (left < right)) left++;

		// right가 피벗보다 크면 계속 right를 감소
		while ((a[right] >= a[pivot]) && (left < right)) right--;

		if (left < right)
		{
			temp = a[left];
			a[left] = a[right];
			a[right] = temp;

			if (left == pivot)
				pivot = right;
		}
	}
	temp = a[pivot];
	a[pivot] = a[right];
	a[right] = temp;

	return right;
}

void quickSort(int a[], int p, int r)
{
	if (p < r)
	{
		int q = partition(a, p, r);
		quickSort(a, p, q - 1);
		quickSort(a, q + 1, r);
	}
}

int main(void)
{
	int list[5] = { 3, 5, 1, 4, 2 };

	quickSort(list, 0, size-1);

	for (int i = 0; i < size; i++)
	{
		printf("%d\n", list[i]);
	}

	return 0;
}
```
-------------
