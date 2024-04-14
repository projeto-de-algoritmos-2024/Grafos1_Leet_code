class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
      n = len(graph)
          
        
#Testar uma BFS para encontrar o caminho mais curto.
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

    return #Se solução for encontrada
