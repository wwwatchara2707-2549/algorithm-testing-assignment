def two_characters(s):
    unique_chars = list(set(s))
    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]

            filtered = [c for c in s if c == c1 or c == c2]

            valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    valid = False
                    break

            if valid and len(filtered) >= 2:
                max_length = max(max_length, len(filtered))

    return max_length