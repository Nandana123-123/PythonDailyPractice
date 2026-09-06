def getDivisors(n):
    res = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.append(i)

            if i != n // i:
                res.append(n // i)

    res.sort()
    return res


n=int(input("Enter a number: "))
print(getDivisors(n))