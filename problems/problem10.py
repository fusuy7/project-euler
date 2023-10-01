def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def PrimeSum(n):
    l = []
    for i in range(n):
        if isPrime(i) is True:
            l.append(i)
    return sum(l)

print(PrimeSum(2000000))