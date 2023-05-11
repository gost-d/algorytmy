import scipy.special

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


print("RANK: " + str(rank([5,2,1],5)))
print("UNRANK: " + str(unrank(20, 5, 3)))




////////////////////////////////////
///////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////
################################################################################################################3
###############################################################################################################################

import scipy.special

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
    
    for i in range ( k - 1, 0, -1 ):
        if ( t[k-i] + 1 < t[k-i-1] ):
            t[k-i] = t[k-i] + 1
            return t

    if ( t[0] < n ):
        t[0] = t[0] + 1
        for i in range ( 1, k ):
            t[k-i] = i
        return t
    #
    for i in range ( 1, k + 1 ):
        t[i-1] = k + 1 - i

    return t


print("RANK: " + str(rank([5,2,1],5)))
print("UNRANK: " + str(unrank(20, 5, 3)))
print("SUCCESSOR: " + str(successor(5,3,[5,4,1])))
