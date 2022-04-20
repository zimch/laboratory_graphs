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
    
def about_raskr(G):
    V = list(G.keys())
    C = [0 for i in range(len(V))]
    
    for v in V:
        A = [i for i in range(1, len(V) + 1)]
        for u in G[v]:
            if C[u] in A:
                A.remove(C[u])
            else:
                continue
        
        C[v] = min(A)
        
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

