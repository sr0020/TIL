# Sorting1 (Selection, Bubble, Insertion Sort)
---------------------
## Selection Sort
+ 수도 코드
```C
selectionSort(A[], n)
{
  for last <- n downto 2
  {
    A[1 ... Last] find the largest element A[k];
    A[k] <-> A[last]; (exchange A[k] with A[last])
  }
}
```

```C
#include <stdio.h>

void selectionSort(int A[], int size)
{
	int i, j, min, temp;

	for (int i = 0; i < size - 1; i++)
	{
		min = i;

		for (int j = i+1; j < size; j++)
		{
			if (A[j] < A[min])
				min = j;
		}
		temp = A[i];
		A[i] = A[min];
		A[min] = temp;
	}

	for (int t = 0; t < size; t++)
	{
		printf("%d\n", A[t]);
	}
}

int main(void)
{
	int list[5] = { 3, 4, 2, 1, 5 };
	int size = 5;

	selectionSort(list, size);

	return 0;
}
```
---------------------
## Bubble Sort
+ 수도 코드
```C
BubbleSort(A[], n)
{
  for last <- n downto 2
    for i <- 1 to last <- n 
      if (A[i] > A[i+1]) then A[i] <-> A[i+1];
}
```

```C
#include <stdio.h>

void bubbleSort(int A[], int size)
{
	int i, j, min, temp;

	for (int i = size-1; i > 0; i--) 
	{
		for (int j = 0; j < i; j++)
		{
			if (A[j] > A[j + 1])
			{
				temp = A[j];
				A[j] = A[j + 1];
				A[j + 1] = temp;
			}
		}
	}

	for (int t = 0; t < size; t++)
	{
		printf("%d\n", A[t]);
	}
}

int main(void)
{
	int list[5] = { 3, 4, 2, 1, 5 };
	int size = 5;

	bubbleSort(list, size);

	return 0;
}
```
---------------------
## Insertion Sort
+ 수도 코드
```C
InsetionSort(A[], n)
{
  for i <- 2 to n
    A[1 ... i]의 적합한 자리에 A[i]를 삽입한다;
}
```
```C
#include <stdio.h>

void insertionSort(int A[], int size)
{
	int i, j, temp;

	for (int i = 1; i < size; i++)
	{
		temp = A[i];
		j = i;

		// j 값은 음수가 아니어야 되고
    		// temp 값보다 정렬된 배열에 있는 값이 크면 j-1번째를 j번째로 이동
		while((j>0) &&(A[j-1] > temp))
		{
			A[j] = A[j - 1];
			j = j - 1;
		}
		A[j] = temp;
	}

	for (int t = 0; t < size; t++)
	{
		printf("%d\n", A[t]);
	}
}

int main(void)
{
	int list[5] = { 3, 4, 2, 1, 5 };
	int size = 5;

	insertionSort(list, size);

	return 0;
}
```
---------------------
