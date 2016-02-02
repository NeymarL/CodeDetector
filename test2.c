#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{
    char abbreviated[20];
    char name[60];
    char URL[50];
}Web;

int Compare(const void* a, const void* b)
{
    return strcmp(((Web*)a)->abbreviated , ((Web*)b)->abbreviated);
}

int main()
{
    int n, i;
    scanf("%d", &n);
    Web asds[n];
    for(i = 0; i < n; i++){
        scanf("%s %s %s", asds[i].abbreviated, asds[i].name, asds[i].URL);
    }
    for(i = 0; i < n; i++){
        printf("%-20s%-40s%s\n", asds[i].abbreviated, asds[i].name, asds[i].URL);
    }
    printf("\n");
    qsort(asds, n,sizeof(asds), Compare);
    for(i = 0; i < n; i++){
        printf("%-20s%-40s%s\n", asds[i].abbreviated, asds[i].name, web[i].URL);
    }
    return 0;
}
