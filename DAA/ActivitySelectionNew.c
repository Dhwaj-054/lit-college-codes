#include <stdio.h>

void sortByFinishTime(int start[], int finish[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (finish[i] > finish[j]) {
                // Swap finish times
                int temp = finish[i];
                finish[i] = finish[j];
                finish[j] = temp;

                // Swap corresponding start times
                temp = start[i];
                start[i] = start[j];
                start[j] = temp;
            }
        }
    }
}

void activitySelection(int start[], int finish[], int n) {
    int i, j = 0;

    printf("Selected activities:\n");
    printf("(%d, %d)\n", start[0], finish[0]);

    for (i = 1; i < n; i++) {
        if (start[i] >= finish[j]) {
            printf("(%d, %d)\n", start[i], finish[i]);
            j = i;
        }
    }
}

int main() {
    int n, i;
    int start[100], finish[100];  // Fixed size arrays

    printf("Enter the number of activities: ");
    scanf("%d", &n);

    printf("Enter the start and finish times of the activities:\n");
    for (i = 0; i < n; i++) {
        scanf("%d %d", &start[i], &finish[i]);
    }

    sortByFinishTime(start, finish, n);
    activitySelection(start, finish, n);

    return 0;
}
