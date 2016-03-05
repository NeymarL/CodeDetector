#include<stdio.h>
#include<math.h>
#include<time.h>

int main()
{
	int a[10000], i;
	for( i = 1; i < 10000; i++){
		a[i] = i * pow(-1, i);
	}
	start = clock();
	printf("MaxSubseqSum1 = %d\n", MaxSubseqSum1(a, 10000));
	stop = clock();
	printf("算法一运行了%lfs\n", (double)(stop - start) / CLK_TCK);
	start = clock();
	printf("MaxSubseqSum2 = %d\n", MaxSubseqSum2(a, 10000));
	stop = clock();
	printf("算法二运行了%lfs\n", (double)(stop - start) / CLK_TCK);
	start = clock();
	printf("MaxSubseqSum4 = %d\n", MaxSubseqSum4(a, 10000));
	stop = clock();
	printf("算法四运行了%lfs\n", (double)(stop - start) / CLK_TCK);
	return 0;
}

int iaofan(int A[], int N)
{
	int ThisSum, MaxSum = 0;
	int i, j, k;
	for( i = 0; i < N; i++){                  //i是子列左端位置
		for( j = i; j < N; j++){              //j是子列右端位置
			ThisSum = 0;                      // ThisSum 是从A[i]到A[j]的子列和 
			for( k = i; k <= j; k++)        
			    ThisSum += A[k];
            if( ThisSum > MaxSum)
                MaxSum = ThisSum;
		}
	}
	return MaxSum;
}                                 // T(N) = O(N3)

int inclasd(int A[], int N)
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

int ibf2314o4(int A[], int N)
{
	int sss = 0, MaxSum = 0;
	int i;
	for( i = 0; i < N; i++){
		sss += A[i];              //向右累加 
		if( sss > MaxSum)
		    MaxSum = sss;         //发现更大则更新结果 
		else if ( sss < 0)        //如果当前子列和为负 
		    sss = 0;             //则不可能使后面的和增大，抛弃之 
	}
	return MaxSum; 
}                                     //O(N)
