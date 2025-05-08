#include <iostream>
#include <string>

////// To-do: Write Your Code Here//////////////
// Template function mergeArrays()  to merge two arrays
template <typename T>
void mergeArrays(const T *arr1, int size1, const T *arr2, int size2, T *&mergeArray)
{
    int i = 0, j = 0;

    mergeArray = new T[size1 + size2];
    if (arr1 != nullptr)
    {
        while (i < size1)
        {
            mergeArray[i] = arr1[i];
            i++;
        }
    }

    if (arr2 != nullptr)
    {
        while (j < size2)
        {
            mergeArray[i] = arr2[j];
            i++;
            j++;
        }
    }
}

////// To-do: Write Your Code Here//////////////
// Template function printAndDeallocate() to print and deallocate the merged array
template <typename T>
void printAndDeallocate(T *&mergedArray, int size)
{
    std::cout << "Merged Array: ";
    for (int i = 0; i < size; i++)
    {
        std::cout << mergedArray[i] << " ";
    }
    std::cout << std::endl;

    delete[] mergedArray;
    mergedArray = nullptr;
}

int main()
{
    // Case 1: Integers
    int *arr1 = new int[3];
    arr1[0] = 1;
    arr1[1] = 2;
    arr1[2] = 3;
    int size1 = 3;
    int arr2[] = {4, 5, 6};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    int *mergedArray = nullptr;
    // Merging arrays
    mergeArrays(arr1, size1, arr2, size2, mergedArray);
    // Printing and deallocating the merged array
    printAndDeallocate(mergedArray, size1 + size2);
    delete[] arr1;

    // Case 2: doubles
    double arr3[] = {1.1, 2.2, 3.3};
    int size3 = sizeof(arr3) / sizeof(arr3[0]);
    double arr4[] = {4.4, 5.5};
    int size4 = sizeof(arr4) / sizeof(arr4[0]);
    double *mergedArray2 = nullptr;
    mergeArrays(arr3, size3, arr4, size4, mergedArray2);
    printAndDeallocate(mergedArray2, size3 + size4);

    return 0;
}
