#gráf algoritmus (minimum hosszúságú bitstring)
n = int(input())

k = 2

a = [0] * (k * n)
tomb = []

def db(t, p):
    if t > n:
        if n % p == 0: #aktuális szakasz hossza (p) osztója-e n-nek
            tomb.extend(a[1:p+1]) #ha igen akkor hozzáfűzi a kimenethez
    else:
        a[t] = a[t-p] #továbblép a lemásolt periódussal
        db(t+1, p)
        for j in range(a[t-p]+1, k):
            a[t] = j
            db(t+1, t)

db(1, 1)

res = "".join(str(x) for x in tomb) + "0" * (n-1) #a ciklust egy sorozattá alakítja
print(res)
