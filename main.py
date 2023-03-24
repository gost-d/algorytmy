
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














