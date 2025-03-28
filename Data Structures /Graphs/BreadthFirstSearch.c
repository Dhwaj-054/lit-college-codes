// C code for bfs in graph traversal
#include<stdio.h>

#define MAX 5

void bfs(int adj[][MAX],int visited[],int start) {
    int queue[MAX], rear = -1, front = -1, i;
    queue[++rear] = start;
    visited[start] = 1;
    while(rear != front) {
        start = queue[++front];
        if(start == MAX)
            printf("%d\t", MAX);
        else
            printf("%c\t",(start + 65));
        for(i=0 ; i<MAX ; i++) {
            if(adj[start][i] && !visited[i]) {
                queue[++rear] = i;
                visited[i] = 1;
            }
        }
    }
}

int main() {
    int visited[MAX] = {0};
    int adj[MAX][MAX] , i, j;

    printf("\n Enter the adjacency matrix :\n");
    for(i=0;i<MAX;i++)
        for(j=0;j<MAX;j++)
            scanf("%d",&adj[i][j]);

    bfs(adj,visited,0);

    return 0;
}
