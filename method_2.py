import time
import translate
import matplotlib.pyplot as plt
import generator

def delta(G):
    m = -1
    for i in G.keys():
        if len(G[i]) > m: m = len(G[i])
        
    return m

def hi(G):
    return 1 + delta(G) # оценка сверху

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
    
    while V:
        #print(V)
        for v in V:
            try:
                for u in G[v]:
                    #print(v, u, G[v], C, c)
                    if C[u] == c:
                        raise Exception()
                        #break
                
                C[v] = c
                V.remove(v)
            
            except Exception:
                continue
            
        c += 1
        
    return C

times = []
colors = []

for i in range(2, 1000):
    G = translate.translateLook(generator.ER(i, 0.4), i)
    start_time = time.time()
    C = about_raskr(G)
    times.append(time.time() - start_time)
    colors.append(max(C))
    # print(about_raskr(G))
    

# print(colors)
print(times)


# G1 = {
#     0 : [1, 3],
#     1 : [0, 2],
#     2 : [1, 3],
#     3 : [0, 2]
# }

# G2 = {
#     0 : [],
#     1 : [2],
#     2 : [1]
# }

# G3 = {
#     0 : [1, 2, 3],
#     1 : [0, 2],
#     2 : [1, 0, 3, 4],
#     3 : [0, 2, 4],
#     4 : [3, 2]
# }

# G4 = {
#     0 : [1],
#     1 : [0, 2],
#     2 : [1]
# }

# print(sort(G3, G3.keys()))
# print(about_raskr(G1))
# print(about_raskr(G2))
# print(about_raskr(G3))
# print(about_raskr(G4))