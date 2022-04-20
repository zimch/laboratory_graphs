from translate import translateLook
from generator import ER
from goto import with_goto

n = 10
G = translateLook(ER(n, 0.4), n)

@with_goto
def maxset(G):
    k = 0
    S = [None for i in range(n)]
    
    