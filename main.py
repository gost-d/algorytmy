
import scipy.special

def rank(T, n):
    r = 0
    k = len(T)
    T.insert(0,0)

    for i in range(1, k+1):
        if T[i-1] + 1 <= T[i] - 1:
            for j in range(T[i-1] + 1, T[i]):
                r += scipy.special.comb(n-j,k-i)

    i = 0
    while i < k:
        r += scipy.special.comb(n,i)
        i += 1

    return r


def unrank(r, n):

    k = 0
    T = []
    x = 1

    if r == 0:
        print("Unrank: []")

    while scipy.special.comb(n,k) <= r:
        r = r - scipy.special.comb(n,k)
        k = k + 1

    for i in range(1,k+1):
        while scipy.special.comb(n-x,k-i) <= r:
            r = r - scipy.special.comb(n-x,k-i)
            x = x + 1
        T.insert(i,x)
        x = x + 1

    return T


def successor2(rank,n):
    T = unrank(rank,n)
    U = T.copy()
    k = len(T)
    i = k
    if len(U) == 0:
        U.append(1)
        return U

    while i >= 0 and T[i-1] == n - k + i:
        i -= 1

    if k == n:
        return None
    elif sum(T) == sum(list(range(n,n-len(T),-1)))  :
        U.append(0)
        for x in range(1,len(T)+2):
            U[x-1] = x
        return U
    else:
        for j in range(i, k+1):
           U[j-1] = T[i-1] + 1 + j - i
        return U


def precedessor(r,n):
    return unrank(r-1,n)



print("RANK: " + str(rank([1,3,4,5],8)))
print("UNRANK: " + str(unrank(26, 5)))
print("SUCCESSOR: " + str(successor2(22,5)))
print("PRECEDESSOR: " + str(precedessor(108,8)))



/////////////////////////////////////

///////////////////////////////////


def successor(n, k, t):
    
    #Tutaj sprawdzamy, czy jest różnica większa niż 1 między elementami. Jeśli tak - robimy +1 na danym elemencie. I reszta zostje tak samo. 

    for i in range (0, k):
        if ( t[k-i-1] + 1 < t[k-i-2] ):
            t[k-i-1] = t[k-i-1] + 1
            return t
    #Jeśli nie było takie różnicy, to znaczy że musimy podbić pierwszą cyferkę, bo mamy układy w stylu 432, 543 itp. - czyli żeby to zwiększyć, to rzeba rzejść wyżej
    #przy peirwszej cyferce. Dodajemy 1 do pierwszej, a potem jeszcze od tyłu ustawiamy wartości od 1 do tej cyferki, np. 621 --> od tyłu, czyli 1 na koniec, potem 2, no a potem 6

    # if ( t[0] < n ):
    #     t[0] = t[0] + 1
    #     for i in range ( 1, k ):
    #         t[k-i] = i
    #     return t
    #
    t[0] = t[0] + 1
    for i in range ( 1, k ):
        t[k-i] = i
         

    return t














