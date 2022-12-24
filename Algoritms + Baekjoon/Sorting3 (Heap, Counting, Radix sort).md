# Sorting (Heap, Counting, Radix Sort)
--------------
## Heap Sort
+ 수도 코드
```C
buildHeap(A[], n)
{
	for i <- n/2 downto 1
	heapify(A, i, n);
}
heapify(A[], k, n)
{
	left <- 2k;
	right <- 2k + 1;
	
	if(right <= n) then
	{
		if(A[left] < A[right])
			then smaller <- left;
		else smaller <- right;
	}
	
	else if(left <= n) 
		then smaller <- left;
	else return;
	
	if(A[smaller] < A[k]) then
	{
		A[k] <- A[smaller];
		heapify(A, smaller, n);
	}
}

heapSort(A, n)
{
	buildHeap(A, n);
	for i <- n down to 2 
	{
		A[1] <-> A[i];
		heapify(A, 1, i-1);
	}
}
```
+ 코드
```C
```
------------
## Counting Sort
```C
countingSort(A[], B[], n)
// A[1...n]: 입력 배열
// B[1...n]: 배열 A[]를 정렬한 결과
{
	for i <- 1 to K
		C[i] <- 0;
	for j <- 1 to n
		C[A[j]]++;
		// 이 시점에서 C[i] : 값이 i인 원소의 총수
	for i <- 2 to k
		C[i] <- C[i] + C[i-1];
		// 이 시점에서 C[i]: i보다 작거나 같은 원소의 총수
	for j <- n downto 1
	{
		B[C[A[i]] <- A[j];
		C[A[j]]--;
	}
}
```
------------
## Radix Sort
```C
// 원소들이 각각 최대 K (RADIX) 자릿수인 A[1 .. n]을 정렬한다. (RADIX = 10으로 설정함) (10진수 기수정렬하는 수도코드)
// 가장 낮은 자릿수를 1번째 자릿수라 한다.

radixSort(A[], n) // 자료구조 p534 (알고리즘 아님)
{
	factor <- 1;
	for(k <- 0; k < KEY_DIGIT; k <- k+1) do {
		for(i <- 0; i < n; i <- i+1) do {
			enQueue(Q[(a[i]/factor) mod RADIX], a[i]);
		}
	}
	p <- -1;
	
	// i 번째 자릿 수에 대해 A[1 ... n]을 안정성을 유지하면서 정렬한다.
	for(i = 0; i < RADIX; i <- i+1) do {
		while(Q[i] != NULL) do {
			p <- p+1;
			a[p] <- deQueue(Q[i]);
		}
	}
	factor <- factor * RADIX;
}
```
