from itertools import chain, combinations

from math import fsum

def powerset(M): 
    a=list(chain.from_iterable(combinations(M, r) for r in range(len(M)+1))) #Lista de todos los conjuntos diferentes que se pueden crear
    b=[] #Lista donde se van a almacenar todas las posibles sumas 
    for i in range(len(a)):
        b.append(fsum(a[i]))
    return b,a
    
def pizza (M,N,S):
    S.sort()
    #Sumatorio de todos los trozos de pizza posibles
    Sum=0
    for i in S:
        Sum = Sum+i
    #Diferencia con el máximo impuesto
    Dif = Sum-M
    
    #En el caso de que el número esté en la lista
    if Dif in S:
        K = N-1
        Ind = S.index(Dif)
        L = list(range(len(S)))
        L.remove(Ind)
        print ('K = '+str(K))
        print ('L = '+str(L))
        
    else: #Caso de que el número no esté en la lista
        V = []
        for i in S:
            if i > Dif:
                Lim = i
                break
            else:
                V.append(i) #Lista de números que son menores que Lim
        
        W = powerset(V)[0] #Todas las posibles sumas que se generan con la lista V
        a = powerset(V)[1]
        print(W)
        print(a)
        G = []
        for i in W:
            if ((i < Dif) or (i >= Lim)):
                continue
            else:
                G.append(i)
            
        if G == []:
            K = N-1
            Ind = S.index(Lim)
            L = list(range(len(S)))
            L.remove(Ind)
            print ('K = '+str(K))
            print ('L = '+str(L))
            
        else:
            R = min(G)
            E = W.index(R)
            F = a[E]
            K = N -len(F)
            
            L = list(range(len(S)))
            for i in F:
                Ind = S.index(i)
                L.remove(Ind)
            print ('K = '+str(K))
            print ('L = '+str(L))
                        

pizza(32,5,[3,6,7,10,15])