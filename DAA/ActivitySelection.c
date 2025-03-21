// C code for Activity Selection using the Greedy method

#include <stdio.h>
#include<conio.h>
#include <stdlib.h>
typedef struct {
 int start;
 int finish;
} Activity;
int compare(const void* a, const void* b) {
 Activity* actA = (Activity*)a;
 Activity* actB = (Activity*)b;
 return actA->finish - actB->finish;
}
void activitySelection(Activity activities[], int n) {
 int j=0;
 int i;
 qsort(activities, n, sizeof(Activity), compare);
 printf("Selected activities:\n");
 printf("(%d, %d)\n", activities[j].start, activities[j].finish);
 for (i = 1; i < n; i++) {
 if (activities[i].start >= activities[j].finish) {
 printf("(%d, %d)\n", activities[i].start, activities[i].finish);
 j = i;
 }
 }
}
void main() {
 int n,i;
 Activity* activities = (Activity*)malloc(n * sizeof(Activity));
 printf("Enter the number of activities: ");
 scanf("%d", &n);
 printf("Enter the start and finish times of the activities:\n");
 for (i = 0; i < n; i++) {
 scanf("%d %d", &activities[i].start, &activities[i].finish);
 }
 activitySelection(activities, n);
 getch();
}
