kilometre_1 = float (input ("Please enter the speed of car in Kilometre as a unit: "))
    conversion_ratio_1 = 0.621371
    miles_1 = kilometre_1 * conversion_ratio_1
    print ("The speed value of car in Miles: ", miles_1)
#include<stdio.h>
 int main()
{
int n, reverse=0, rem;
printf("Enter a number: ");
  scanf("%d", &n);
  while(n!=0)
  {
     rem=n%10;
     reverse=reverse*10+rem;
     n/=10;
  }
  printf("Reversed Number: %d",reverse);
return 0;
}
