def compress(chars):
        i = 0
        k = 0

        while i < len(chars):
            ch = chars[i]
            cnt = 0

            while i < len(chars) and chars[i] == ch:
                i += 1
                cnt += 1

            chars[k] = ch
            k += 1

            if cnt > 1:
                for digit in str(cnt):
                    chars[k] = digit
                    k += 1

        return k

chars=list(input("Enter a string: "))
k=compress(chars)
print(k)
#print("compressed string is","".join(k))