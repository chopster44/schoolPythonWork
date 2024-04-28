#include <stdio.h>

#define LEN(x)  (sizeof(x) / sizeof((x)[0]))

void printArray(int *array, int arraySize) {
    printf(" {");
    for (int i = 0; i < arraySize; i++) {
        printf("%i", array[i]);
        if (i < (arraySize - 1)) {
            printf(", ");
        }
    }
    printf("}\n");
}

int main() {
    printf("Unsorted:");
    int array[7] = {3, 9, 2, 10, 8, 5, 1};
    
    int i;
    for (i = 1; i < LEN(array); i++) {
        int j;
        for (j = i; j > 0; j--) {
            if (array[i] < array[j]) {
                int t = array[i];
                array[i] =
                swap(array, LEN(array), i, j);
            }
        } 
    }
    

    printf("Sorted:");
    printArray(array, LEN(array));
}