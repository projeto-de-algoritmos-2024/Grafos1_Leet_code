#BFS(G)
#for every vertex s of G not explored yet
#do Enqueue(S,s);
#mark vertex s as visited
#while S is not empty do
#u ← Dequeue(S);
#For each v in Adj[u] then
#if v is unexplored then
#mark edge (v,u) as tree edge
#mark vertex v as visited
#Enqueue(S,v)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        vetor=[0]*n
        for no in range(n):
            if vetor[no]==0: #Começando apenas se não for colorido
                fila=[(no, 1)]
                i=0
                while (i<len(fila)):
                    atual, cor =fila[i]
                    i =i+1
                    if (vetor[atual]==0):
                        vetor[atual]=cor  #Pintando
