def compress(chars):
    res = []
    i = 0

    while i < len(chars):
        ele = chars[i]
        count = 0

        while i < len(chars) and chars[i] == ele:
            count += 1
            i += 1

        res.append(ele)

        if count > 1:
            for x in str(count):
                res.append(x)

    chars[:] = res

    return len(res)

chars=list(input("Enter a string: "))
compress(chars)
print(chars)