#include <iostream>
#include <vector>
#include <algorithm> // for std::sort
#include <numeric>   // for std::accumulate

int main()
{
    // Declare a vector to store daily sales.
    std::vector<int> dailySales;

    // TO-DO: Add seven daily sales values to the vector:
    //         120, 200, 150, 80, 90, 220, 100
    dailySales = {120, 200, 150, 80, 90, 220, 100};

    // TO-DO: Print all sales values by using an iterator
    std::cout << "Daily Sales: ";
    for (int i : dailySales)
    {
        std::cout << i << ' ';
    }
    std::cout << std::endl;

    // TO-DO: Calculate the average of the sales values and print it
    std::cout << "Average Sales: ";
    double sum = std::accumulate(dailySales.begin(), dailySales.end(), 0.0);
    double average = sum / dailySales.size();
    std::cout << average << std::endl;

    // TO-DO: Sort the vector in ascending order using std::sort.

    std::sort(dailySales.begin(), dailySales.end());

    // TO-DO: Print all the sorted sales values by using an iterator
    std::cout << "Sorted Sales: ";
    for (int j : dailySales)
    {
        std::cout << j << ' ';
    }

    return 0;
}
