#include<stdio.h>
#define SWAP(a,b) (a)=(a)+(b);(b)=(a)-(b);(a)=(a)-(b)

int main()
{
    int n,i;
    scanf("%d",&n);
    for( i = 0; i < n; i ++){
        int a,b;
        scanf("%d %d",&a,&b);
        SWAP(a,b);
        printf("%d %d\n",a,b);
    }
    return 0;
}
