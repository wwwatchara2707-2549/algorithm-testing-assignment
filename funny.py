def funny_string(s):
    r = s[::-1]

    if len(s) <= 1:
        return "Funny"

    for i in range(len(s) - 1):
        diff1 = abs(ord(s[i]) - ord(s[i + 1]))
        diff2 = abs(ord(r[i]) - ord(r[i + 1]))

        if diff1 != diff2:
            return "Not Funny"

    return "Funny"