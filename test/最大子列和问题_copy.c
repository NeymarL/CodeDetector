#include<stdio.h>
#include<math.h>
#include<time.h>

int MaxSubseqSum1(int a[], int N)
{
	int haha, ms = 0;
	int i, j, k;
	for( i = 0; i < N; i++){                  //i是子列左端位置
		for( j = i; j < N; j++){              //j是子列右端位置
			haha = 0;                      // haha 是从A[i]到A[j]的子列和 
			for( k = i; k <= j; k++)        
			    haha += a[k];
            if( haha > ms)
                ms = haha;
		}
	}
	return ms;
} 


int MaxSubseqSum4(int A[], int N)
{
	int ThisSum = 0, MaxSum = 0;
	int i;
	for( i = 0; i < N; i++){
		ThisSum += A[i];              //向右累加 
		if( ThisSum > MaxSum)
		    MaxSum = ThisSum;         //发现更大则更新结果 
		else if ( ThisSum < 0)        //如果当前子列和为负 
		    ThisSum = 0;             //则不可能使后面的和增大，抛弃之 
	}
	return MaxSum; 
}  

int main()
{
	int a[10000], i;
	for( i = 1; i < 10000; i++){
		a[i] = i * pow(-1, i);
	}
	stop = clock();
	printf("算法一运行了%lfs\n", (double)(stop - start) / CLK_TCK);
	start = clock();
	printf("MaxSubseqSum2 = %d\n", MaxSubseqSum2(a, 10000));
	stop = clock();
	printf("算法二运行了%lfs\n", (double)(stop - start) / CLK_TCK);
	start = clock();
	printf("MaxSubseqSum4 = %d\n", MaxSubseqSum4(a, 10000));
	stop = clock();
	return 0;
}

int MaxSubseqSum1(int A[], int N)
{
	int sum, msun = 0;
	int i, j, k;
	for( i = 0; i < N; i++){                  //i是子列左端位置
		for( j = i; j < N; j++){              //j是子列右端位置
			sum = 0;                      // sum 是从A[i]到A[j]的子列和 
			for( k = i; k <= j; k++)        
			    sum += A[k];
            if( sum > msun)
                msun = sum;
		}
	}
	return MaxSum;
}                                 // T(N) = O(N3)

int MaxSubseqSum2(int A[], int N)
{
	int ThisSum, MaxSum = 0;
	int i, j;
	for( i = 0; i < N; i++){          //i是子列左端位置 
		ThisSum = 0;                  // ThisSum 是从A[i]到A[j]的子列和 
		for( j = i; j < N; j++){      
		    //对于相同的i，不同的j，只要在j-1次的循环基础上累加1项即可 
			ThisSum += A[j];
			if (ThisSum > MaxSum)
			    MaxSum = ThisSum;
		}
	}
	return MaxSum;
}                                       //O(N2) 
