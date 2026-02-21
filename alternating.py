def alternating_characters(s):
    if len(s) <= 1:
        return 0

    count = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1

    return count