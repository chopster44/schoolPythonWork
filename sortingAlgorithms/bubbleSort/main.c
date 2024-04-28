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

int checkValues(int *array, int index, int len) {
    if (array[index] > array[index + 1]) {
        int t = array[index];
        array[index] = array[index + 1];
        array[index + 1] = t;
        if (index < (len - 1)) {
            checkValues(array, index + 1, len);
        }
        return 1;
    } else {
        if (index == (len - 1))
            return 0;
        return checkValues(array, index + 1, len);
    }
}

void bubble(int *array, int len) {
    if (checkValues(array, 0, len-1))
        bubble(array, len);
    return;
}

int main() {
    int array[7] = {3, 9, 2, 10, 8, 5, 1};
    printf("Unsorted:");
    printArray(array, LEN(array));

    bubble(array, LEN(array));

    printf("Sorted:");
    printArray(array, LEN(array));
}