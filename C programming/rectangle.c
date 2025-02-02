#include <stdio.h>
int main()
{
    float length, width,area, perimetre;
    printf("Enter the Length and width of the rectangle : \n");
    scanf("%f%f",&length,&width);
    area=length*width;
    perimetre=2*(length+width);
    printf("The area of the rectangle is %f \n The perimetre of the rectangle is %f \n ",area,perimetre);
    return 0;
}