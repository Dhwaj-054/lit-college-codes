#include <stdio.h>

void frac(int p[], int w[], int cap, int n);

int main() {
    int p[] = {24, 15, 25};
    int w[] = {15, 10, 18};
    int cap = 20;
    int n = sizeof(p) / sizeof(p[0]);

    frac(p, w, cap, n);

    return 0;
}

void frac(int p[], int w[], int cap, int n) {
    float pw[100];  // assuming max 100 items
    float tempratio;
    int i, j, temprofit, tempweight;
    float totalprofit = 0;

    // Calculate profit/weight ratio
    for(i = 0; i < n; i++) {
        pw[i] = (float)p[i] / w[i];
    }

    // Sort by descending pw ratio using bubble sort
    for(i = 0; i < n - 1; i++) {
        for(j = 0; j < n - 1 - i; j++) {
            if(pw[j] < pw[j + 1]) {
                // Swap ratios
                tempratio = pw[j];
                pw[j] = pw[j + 1];
                pw[j + 1] = tempratio;

                // Swap profits
                temprofit = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temprofit;

                // Swap weights
                tempweight = w[j];
                w[j] = w[j + 1];
                w[j + 1] = tempweight;
            }
        }
    }

    printf("Items selected:\n");
    for(i = 0; i < n; i++) {
        if(cap >= w[i]) {
            cap -= w[i];
            totalprofit += p[i];
            printf("Item %d: 100%% taken (Profit: %d, Weight: %d)\n", i + 1, p[i], w[i]);
        } else {
            float frac = (float)cap / w[i];
            totalprofit += p[i] * frac;
            printf("Item %d: %.2f%% taken (Profit: %.2f, Weight: %d)\n", i + 1, frac * 100, p[i] * frac, cap);
            break; // knapsack is full
        }
    }

    printf("Total Profit: %.2f\n", totalprofit);
}
