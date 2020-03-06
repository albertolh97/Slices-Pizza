def pizza (M,N,S):
    
    #Sumatorio de todos los trozos de pizza posibles
    Sum=0
    for i in S:
        Sum = Sum+i
    #Diferencia con el máximo impuesto
    Dif = Sum-M
    #Buscar lo que sobre
    if Dif in S:
        K = N-1
        Ind = S.index(Dif)
        L = list(range(len(S)))
        L.remove(Ind)
        return K,L
    return K,L

print (pizza(25,5,[2,5,8,10,12]))