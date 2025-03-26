//this is the code in C for Kruskals algorithm 

#include <stdio.h>
#include <stdlib.h>

#define MAX 100
#define INF 99999

typedef struct {
    int u, v, weight;
} Edge;

Edge edges[MAX];
int parent[MAX];
int rank[MAX];
int numEdges = 0;

void initialize(int vertices) {
    for (int i = 0; i < vertices; i++) {
        parent[i] = i;
        rank[i] = 0;
    }
}

int find(int i) {
    if (parent[i] != i) {
        parent[i] = find(parent[i]); 
    }
    return parent[i];
}

void unionSets(int u, int v) {
    int rootU = find(u);
    int rootV = find(v);
    
    if (rootU != rootV) {
        if (rank[rootU] > rank[rootV]) {
            parent[rootV] = rootU;
        } else if (rank[rootU] < rank[rootV]) {
            parent[rootU] = rootV;
        } else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
    }
}

int compareEdges(const void *a, const void *b) {
    return ((Edge *)a)->weight - ((Edge *)b)->weight;
}

void kruskal(int vertices) {
    int totalCost = 0;
    int edgesInMST = 0;

    qsort(edges, numEdges, sizeof(edges[0]), compareEdges);

    printf("\nEdge \tWeight\n");
    for (int i = 0; i < numEdges; i++) {
        int u = edges[i].u;
        int v = edges[i].v;
        int weight = edges[i].weight;

        if (find(u) != find(v)) {
            unionSets(u, v);
            printf("%d <-> %d \t%d\n", u, v, weight);
            totalCost += weight;
            edgesInMST++;
        }

        if (edgesInMST == vertices - 1) {
            break;
        }
    }

    printf("Total Cost = %d\n", totalCost);
}

int main() {
    int vertices, edgesCount;

    printf("Enter number of vertices: ");
    scanf("%d", &vertices);
    printf("Enter number of edges: ");
    scanf("%d", &edgesCount);

    printf("Enter edges (u, v, weight):\n");
    for (int i = 0; i < edgesCount; i++) {
        scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].weight);
        numEdges++;
    }

    initialize(vertices);
    kruskal(vertices);

    return 0;
}
