// Online C compiler to run C program online
#include <stdio.h>
int main() 
{
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the elements:\n");
    for (int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    int b;
    printf("Enter the number to be searched: ");
    scanf("%d",&b);
    int found=0;
    for (int i=0;i<n;i++)
    {
        if (a[i]==b)
        {
            printf("The position of the number is: %d",i+1);
            found=1;
            break;  
        }
    }    
    if(!found)
        {
            printf("Not Found");
        }
}
