def TRIM(L:list,d:float) -> list:
    """
    Donde L tiene que estar ordenada en forma desc y 0<d<1
    """
    m = len(L)
    #recordando que L
    L2 = []
    L2.append(L[0])
    last = L[0]
    for i in range(1,m):
        if L[i] > last*(1+d):
            L2.append(L[i])
            last = L[i]
    return L2

def MERGE_LIST(L1:list,L2:list) -> list:
    """
    Ya tu sabhe merge list
    dos lista de enteros ordenadas
    que se juntan, nota por el libro,
    valores duplicado eliminados
    """
    Lz = []
    n = len(L1) + len(L2)
    x = 0
    y = 0
    for i in range(0,n):
        if x == len(L1):
            return list(set(Lz + L2[y:]))

        if y == len(L2):
            return list(set(Lz + L1[x:]))
            
        if L1[x] <= L2[y]:
            Lz.append(L1[x])
            x+=1
        else:
            Lz.append(L2[y])
            y+=1
        
    return list(set(Lz))

def MERGE_LIST2(L1:list,L2:list) -> list:
    Lz = L1 + L2
    Lz = set(Lz)
    Lz = list(Lz)
    Lz.sort()
    return Lz

#print(MERGE_LIST2([0,14],[5,19])) esto porque tuve un conflicto con duplicados
#es medio trampa

def leSumL(L:list,x:int) -> list:
    """
    el ya tu sabhe del libro de L+x
    L lista de enteros que a todo elemento de L
    se le suma x
    """
    Lx = []
    for i in range(0,len(L)):
      Lx.append(L[i]+x)

    return Lx


def removeAllG(L:list,x:int) -> list:
    """
    devulve una lista sin todas las ocurrencias de los
    elementos mayores a x conservando el orden relativo de los
    elementos
    """
    Lf = []
    for i in range(0,len(L)):
        if L[i] <= x:
            Lf.append(L[i])

    return Lf


def APPROX_SUBSET_SUM(S:list,t:int,e:int) -> list:
    """
    algoritmo del libro [Thomas H. Cormen] Introduction to Algorithms
    recuperacion extra, ejercicio 35.5-5 (ya habra otra ocasion)
    """
    n = len(S)
    L = [0] #L0
    for i in range(0,n):
        L = MERGE_LIST2(L,leSumL(L,S[i]))
        L = TRIM(L,e/(2*n))
        L = removeAllG(L,t)
    z = L[-1] #por los merges el mas grande se encuentra al final
   
    return [z, L]


def recuperarD(L:list) -> list:
    #sospecho que L es la lista que provoca la suma de z sin L[-1] y L[0]
    #pero mejor, la idea esta en que la lista recuperada si contiene
    #los valores que provocaron el elemento de su ultima posicion
    #porque son construidas las {x1,x2,...,xi} con las {x1,x2,...,xi-1}
    #y como estan ordenadas las encuentro iterando
    """
    Osea los elementos de S original tendrian que haber estado en la
    L final provacndo el maximo valor
    """
    Ld = L.copy() #para modificar a gusto
    Ld.pop(0) #simepre es 0
    t = Ld.pop()

    Ls = [Ld[0]] #empezando con el primero
    suma = Ls[0]
    for i in range(1,len(Ld)):
        if (suma + Ld[i]) <= t:
            suma += Ld[i]
            Ls.append(Ld[i])
    return Ls

def da_arr_posi():
    """
    un entero positivo n
    """
    while True:
        try:
            n = int(input('¿Cuantos elementos tendra la lista? '))
            if n > 0:
                return llena_arr_posi(n)
            else:
                print('Prueva con un numero mayor que 0')
        except ValueError:
            print('Entrada invalida, intentalo de nuevo')

def llena_arr_posi(n:int) -> list:
    """
    Llenado correcto
    """
    while True:
        try:
            S = []
            for i in range(0,n):
                print('Escribe el', (i+1), "elemento(numero)")
                x = int(input())
                if x <= 0:
                    raise ValueError
                else:
                    S.append(x)
            return S
        except ValueError:
            print('Entrada invalida, intentalo de nuevo')

def da_meta_val(S:list) -> int:
    """
    la meta estara 0<t<= Suma de S, porque es max a encontrar
    """
    while True:
        try:
            tope = sum(S)
            print('Da un numero objetivo t, positivo menor o igual a', tope)
            t = int(input())
            if t > 0 and t <= tope:
                return t
            else:
                raise ValueError
        except ValueError:
            print('El numero no se encuentra en el rango adecuado,',
                  'intentalo de nuevo')

def da_epsilon_val() -> int:
    """
    0 < e < 1
    """

    while True:
        try:
            e = float(input('Elige una \u03B5 entre 0<\u03B5<1\n'))
            if 0 < e and e < 1:
                return e
            else:
                raise ValueError
        except ValueError:
            print('Valor de \u03B5 invalido, intentalo de nuevo')

def nota():
    print('En el problema de optimización, deseamos encontrar\n',
          'un subconjunto de {x1,x2, ... , xn} cuya suma es\n',
          'tan grande como sea posible pero no mayor que t')
    print('El algoritmo de esquema de aproximacion de tiempo\n',
          'completamente polinomial de la pagina 1131 del libro\n',
          '[Thomas H. Cormen] Introduction to Algorithms, solo devuelve\n',
          'un valor z cuyo valor está dentro de un factor (1+\u03B5) de\n',
          'la solución óptima')


def recomen():
    print('Ejemplo del libro:')
    print('S = [104,102,201,101]')
    print('t = 308')
    print('\u03B5 = 0.40')
    print('Resultado z = 302')
    print('Que está dentro de \u03B5 = 40% de la respuesta óptima\n',
          '307 = 104 + 102 + 101; de hecho, está dentro del 2%')

def main():
    print('Esquema de aproximación de tiempo completamente polinomial')
    print('APPROX_SUBSET_SUM(S,t,\u03B5)')
    nota()
    recomen()
    print('Elije tus parametros')
    S = da_arr_posi()
    t = da_meta_val(S)
    e = da_epsilon_val()
    print('APPROX_SUBSET_SUM con',end=' ')
    print(S,end=', ')
    print(t,end=', ')
    print(e, end=' es:\n')
    res = APPROX_SUBSET_SUM(S,t,e)
    print(res[0])
    #print('Con el subconjunto que lo provoco: ', end='')
    #print(recuperarD(res[-1]),end='suma = ')
    #print(sum(recuperarD(res[-1])))
    #print(res[-1])
    #falto tiempo para resolver el 35.5-5
main()



        
      
