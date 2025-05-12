#include <stdio.h>
#include <string.h>

#define d 256 // Number of characters in the input alphabet
#define q 101 // A prime number for hashing

void rabinKarp(char text[], char pattern[]) {
    int n = strlen(text);     // Length of text
    int m = strlen(pattern);  // Length of pattern
    int i, j;
    int p = 0;  // Hash value for pattern
    int t = 0;  // Hash value for text window
    int h = 1;

    // The value of h would be "pow(d, m-1)%q"
    for (i = 0; i < m - 1; i++)
        h = (h * d) % q;

    // Calculate the hash value of pattern and first window of text
    for (i = 0; i < m; i++) {
        p = (d * p + pattern[i]) % q;
        t = (d * t + text[i]) % q;
    }

    // Slide the pattern over text one by one
    for (i = 0; i <= n - m; i++) {
        // If hash values match, check characters one by one
        if (p == t) {
            for (j = 0; j < m; j++) {
                if (text[i + j] != pattern[j])
                    break;
            }
            if (j == m)
                printf("Pattern found at index %d\n", i);
        }

        // Calculate hash value for next window of text
        if (i < n - m) {
            t = (d * (t - text[i] * h) + text[i + m]) % q;

            // Make sure t is positive
            if (t < 0)
                t = t + q;
        }
    }
}

int main() {
    char text[] = "ABCCDDAEFG";
    char pattern[] = "CDD";
    rabinKarp(text, pattern);
    return 0;
}
