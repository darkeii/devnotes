// providing a radius will calculate the area, surface area , volume of a sphere...

#include <stdio.h>
#include <math.h>

int main() {

    double radius = 0.0, area = 0.0, surfacearea = 0.0, volume = 0.0;
    const double PI = 3.14159;

    printf("Enter the radius: ");
    scanf("%lf", &radius);

    area = PI * pow(radius, 2);
    surfacearea =  4 * PI * pow(radius, 2);
    volume = (4 * PI * pow(radius, 3))/3;

    printf("Area: %lf\n", area);
    printf("SurfaceArea: %lf\n", surfacearea);
    printf("Volume: %lf\n", volume);

    return 0;
}