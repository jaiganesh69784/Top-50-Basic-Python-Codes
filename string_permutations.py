def permute(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i in range(len(s)):
        for p in permute(s[:i] + s[i+1:]):
            perms.append(s[i] + p)
    return perms
