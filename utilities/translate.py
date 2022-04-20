import generator

def translateLook(G, n):
    Gtr = {}
    for i in range(n):
        Gtr[i] = []
        
    for edge in G.edges():
        #print(edge[0], edge[1])
        Gtr[edge[0]].append(edge[1])
        Gtr[edge[1]].append(edge[0])
        
        
    return Gtr

