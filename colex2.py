import scipy.special
import unittest

def rank(T, n):
    r = 0
    k = len(T)
    T.insert(0,0)

    for i in range(1, k+1):
        r += scipy.special.comb(T[i] - 1, k + 1 - i)

    i = 0
    while i < k:
        r += scipy.special.comb(n,i)
        i += 1

    return r


def unrank(r, n, k):

    T = []
    x = n

    if r == 0:
        print("Unrank: []")

    i = 0
    while i < k:
        r -= scipy.special.comb(n,i)
        i += 1

    for i in range(1 , k+1):
        while(r < scipy.special.comb(x, k + 1 - i)):
            x = x - 1
        T.insert(i,x+1)
        r -= scipy.special.comb(x, k + 1 - i)
    
    return T


def successor(n, k, t):
    
    #Tutaj sprawdzamy, czy jest różnica większa niż 1 między elementami. Jeśli tak - robimy +1 na danym elemencie. I reszta zostje tak samo. 

    for i in range (0, k):
        if ( t[k-i-1] + 1 < t[k-i-2] ):
            t[k-i-1] = t[k-i-1] + 1
            return t
    #Jeśli nie było takie różnicy, to znaczy że musimy podbić pierwszą cyferkę, bo mamy układy w stylu 432, 543 itp. - czyli żeby to zwiększyć, to rzeba rzejść wyżej
    #przy peirwszej cyferce. Dodajemy 1 do pierwszej, a potem jeszcze od tyłu ustawiamy wartości od 1 do tej cyferki, np. 621 --> od tyłu, czyli 1 na koniec, potem 2, no a potem 6

    if ( t[0] < n ):
        t[0] = t[0] + 1
        for i in range ( 1, k ):
            t[k-i] = i
        return t
    
    

    return "UNDEFINED"


print("RANK: " + str(rank([6,3,1],8)))
print("UNRANK: " + str(unrank(48, 8, 3)))
print("SUCCESSOR: " + str(successor(5,3,[4,2,1])))

assert rank([5,2,1],5) == rank(unrank(20, 5, 3),5)
assert rank([5,3,2],5) == rank(unrank(22, 5, 3),5)
assert rank([4,3,2],5) == rank(unrank(19, 5, 3),5)
assert rank([3,2,1],5) == rank(unrank(16, 5, 3),5)
assert rank([4,3,1],5) == rank(unrank(18, 5, 3),5)
assert rank([5,2],7) == rank(unrank(15, 7, 2),7)
assert rank([5,2],7) == rank(unrank(15, 7, 2),7)
assert rank([5,3,2,1],7) == rank(unrank(65, 7, 4),7)
assert rank([4,2,1],5) == rank(unrank(17, 5, 3),5)
assert rank([6,3,1],8) == rank(unrank(48, 8, 3),8)
