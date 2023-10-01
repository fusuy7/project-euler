def SumOfSquares(n):
    l = []
    for i in range(n + 1):
        s = i ** 2
        l.append(s)
    return sum(l)

def SquareOfSums(n):
    l = []
    for i in range(n + 1):
        l.append(i)
    sums = sum(l)
    return sums ** 2
print(SquareOfSums(100) - SumOfSquares(100))
