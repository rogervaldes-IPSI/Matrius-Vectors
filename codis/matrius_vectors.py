def mostra_matriu(A):
    for fila in A:
        print(fila)
    return

def matriu_zeros(N,M):
    A_zeros = []
    for i in range(N):
        fila_zeros = []
        for j in range(M):
            fila_zeros.append(0)
        A_zeros.append(fila_zeros)
    return A_zeros

def suma_matrius(A,B):
    N = len(A)
    M = len(A[0])
    C = matriu_zeros(N,M)
    for i in range(N):
        for j in range(M):
            C[i][j] = A[i][j]+B[i][j]
    return C

def combinacio_lineal_matrius(llista_matrius, llista_parametres):
    N = len(llista_matrius[0])
    M = len(llista_matrius[0][0])
    A = matriu_zeros(N,M)

    for i in range(len(llista_matrius)):
        A = suma_matrius(A, prod_matriu_escalar(llista_matrius[i],llista_parametres[i]))
    return A

def I(N):
    In = []
    for i in range(N):
        fila = []
        for j in range(N):
            if i== j:
                fila.append(1)
            else:
                fila.append(0)
        In.append(fila)
    return In

def E(i,j,N):
    En = []
    for j1 in range(N):
        fila = []
        for i1 in range(N):
            if i==i1 and j == j1:
                fila.append(1)
            else:
                fila.append(0)
        En.append(fila)
    return En

def prod_matriu_escalar(A,k):
    N,M = len(A), len(A[0])
    for i in range(N):
        for j in range(M):
            A[i][j]*=k
    return A

def P(i,j,N):
    llista_matrius=[I(N),E(i,i,N),E(j,j,N),E(i,j,N), E(j,i,N)]
    parametres = [1,-1,-1,1,1]
    return combinacio_lineal_matrius(llista_matrius,parametres) 

def S(i,j,k,N):
    return I(N) +prod_matriu_escalar(E(i,j,N),k)

def M(i,a,N):
    return I(N)+prod_matriu_escalar(E(i,i,N),a-1)

print("P")
mostra_matriu(P(1,4,5))
print("M")
mostra_matriu(M(3,8,5))
print("S")
mostra_matriu(S(1,4,8,5))

    
