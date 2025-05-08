#include <iostream>
template <typename T>
T getMax(T a, T b)
{
    return (a < b) ? b : a;
}
int main()
{
    int i = 5, j = 10;
    std::cout << "Max(i, j): " << getMax(i, j) << std::endl;
    double x = 5.5, y = 2.3;
    std::cout << "Max(x, y): " << getMax(x, y) << std::endl;
    char c1 = 'a', c2 = 'z';
    std::cout << "Max(c1, c2): " << getMax(c1, c2) << std::endl;
    return 0;
}
