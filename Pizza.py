from itertools import chain, combinations

from math import fsum

#Se crea una función que dada una lista de números es capaz de obtener todas sus posibles combinaciones y la suma de cada combinación
def powerset(M): 
    Conjuntos = list(chain.from_iterable(combinations(M, r) for r in range(len(M)+1))) #Lista de todos los conjuntos diferentes que se pueden crear
    Comb=[] #Lista donde se van a almacenar todas las posibles sumas 
    for i in range(len(Conjuntos)):
        Comb.append(fsum(Conjuntos[i]))
    return Comb,Conjuntos
    
def pizza (M,N,S):
    S.sort()
    #Sumatorio de todos los trozos de pizza posibles
    Sum=0
    for i in S:
        Sum = Sum+i
    #Diferencia con el máximo impuesto
    Dif = Sum-M
    
    #En el caso de que Dif esté directamente en la lista
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
                Lim = i #Número de la lista inmediatamente superior a Dif
                break
            else:
                V.append(i) #Lista de números que son menores que Lim
        
        Comb = powerset(V)[0] #Todas las posibles sumas que se generan con la lista V
        Conjuntos = powerset(V)[1] #Para saber que números generan cada suma
        G = []
        for i in Comb:
            if ((i < Dif) or (i >= Lim)):
                continue
            else:
                G.append(i) #Aquí se almacenan los números de sumas que dan mejores resultados que el valor Lim
            
        if G == []: #Caso de que Lim es la mejor aproximación
            K = N-1
            Ind = S.index(Lim)
            L = list(range(len(S)))
            L.remove(Ind)
            print ('K = '+str(K))
            print ('L = '+str(L))
            
        else: #Caso en el que hay una suma de números que aproxima mejor que Lim
            Aprox = min(G) #Suma que mejor aproxima
            Pos = Comb.index(Aprox) #índice de la suma que mejor aproxima
            Conj = Conjuntos[Pos]  #Conjunto de números que da la mejor suma
            K = N -len(Conj) #Número de pizzas pedidas
            
            #Se eliminan los índices de los números que daban la mejor suma
            #El pedido final es aquello que no se ha eliminado, es decir los elementos que no formaban parte del conjunto con mejor aproximación
            L = list(range(len(S)))
            for i in Conj:
                Ind = S.index(i)
                L.remove(Ind)
            print ('K = '+str(K))
            print ('L = '+str(L))
                        

pizza(101,8,[3,6,7,10,15,23,29,31])