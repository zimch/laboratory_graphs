def d(v):
    return len(v)

def sort(G, V):
    Vs = {}
    for i in V:
        Vs[i] = d(G[i])
        
    sorted_values = sorted(Vs.values()) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in Vs.keys():
            if Vs[k] == i:
                sorted_dict[k] = Vs[k]
            
    return sorted_dict

def about_raskr(G):
    V = list(reversed(list(sort(G, list(G.keys())).keys())))
    C = [0 for i in range(len(list(G.keys())))]
    c = 1
    C[V[0]] = c
    
    while 0 in C:
        for v in V:
            for u in G[v]:
                if C[u] == c:
                    break
            
