def mostra_matriu(A):
    for fila in A:
        print(fila)
    return

def buscar_pivot(A,i):
    el_max = abs(A[i][i])
    index_max = i
    for index in range(i+1,len(A)):
        if abs(A[index][i]) > el_max:
            el_max = abs(A[index][i])
            index_max = index
    return index_max

def intercanvi_files(A,i,fila_pivot):
    fila_auxiliar = A[i]
    A[i] = A[fila_pivot]
    A[fila_pivot] = fila_auxiliar
    return A

def triangulitzar_gauss(A,eps=1e-12):
    n = len(A)
    m = len(A[0])
    swaps=0
    for i in range(n):
        fila_pivot = buscar_pivot(A,i)
        if fila_pivot != i:
            A = intercanvi_files(A,i,fila_pivot)
            swaps +=1
        if abs(A[i][i]) < eps:
            continue
        for j in range(i+1,n):
            pivot = A[j][i]/A[i][i]
            for col in range(i,m):
                A[j][col] = A[j][col]-A[i][col]*pivot
    return A, swaps


def reduir_matriu(A,i,j):
    n=len(A)
    B = []
    fila = 0
    for a in range(n):
        if a == i:
            continue
        B.append([])
        for b in range(n):
            if b==j:
                continue
            B[fila].append(A[a][b])
        fila += 1
    return B

def determinant(A):
    n=len(A)
    if n == 1:
        return A[0][0] 
    det = 0
    for i in range(0,n):
        A_reduida = reduir_matriu(A,0,i)
        det += (-1)**(i)*A[0][i]*determinant(A_reduida)
    return det  

A=[[0,3,6],[8,6,12],[12,2,2]]
mostra_matriu(A)
j=0
det = determinant(A)
diag, swaps = triangulitzar_gauss(A)

print("\n")

mostra_matriu(diag)
det2 = (-1)**swaps
for i in range(len(diag)):
    det2 *= diag[i][i]

det3 = (-1)**swaps*determinant(diag)

print(f"Determinant:{det}")
print(f"Determinant2:{det2}")
print(f"Determinant3:{det3}")