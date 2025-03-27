// C code for the 0/1 Knapsack problem using Greedy approach 

#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int W, int wt[], int val[], int n) {
    int i, w;
    int **K = (int **)malloc((n + 1) * sizeof(int *));
    for (i = 0; i <= n; i++) {
        K[i] = (int *)malloc((W + 1) * sizeof(int));
    }
    // Build K[][] in bottom-up manner
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                K[i][w] = 0; // Base case: no items or capacity
            } else if (wt[i - 1] <= w) {
                // If the current item's weight is less than or equal to the current capacity,
                // consider the maximum of including and excluding the current item
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            } else {
                // If the current item's weight is greater than the current capacity,
                // exclude the current item
                K[i][w] = K[i - 1][w];
            }
        }
    }
    return K[n][W]; 
}

void main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50; 
    int n = sizeof(val) / sizeof(val[0]);
    clrscr();
    printf("Maximum value that can be obtained = %d\n", knapsack(W, wt, val, n));
    getch();
}
