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

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph) #Conta tudo dentro.
        todosnos = (2**n) - 1  #Valor de quando os nos são visitados
        visitados = set()  # Conjunto para armazenar os estados visitados
        fila = [] #Cria fila
        for i in range(n): #Inicializando fila com nós iniciais
            fila.append((i, 2**i))     
        aresta = 0  #Contador de arestas andadas       
        while fila:
            tamanho = len(fila)
            for x in range(0, tamanho):
                no, estado = fila.pop(0)
                if todosnos==estado:
                    return aresta
                if (no,estado) in visitados:continue
                visitados.add((no,estado))
                for vizinho in graph[no]:
                    fila.append((vizinho, estado | (2**vizinho))) 
            aresta=aresta+1
        return -1