#Caesar cipher module by arfur

def encode(text, shift):
    import string
    s = [*text]
    lalf = [*string.ascii_lowercase]
    ualf = [*string.ascii_uppercase]
    if shift <= 0:
        index = 0
    else:
        index = shift
    if index > 26:
        while index > 26:
            index -= 26

    for i in range(0, len(s)):
        if s[i] in lalf:
            c = lalf.index(s[i])
            if c + index < 26:
                s[i] = lalf[c + index]
            else:
                s[i] = lalf[c + index - 26]
        elif s[i] in ualf:
            c = ualf.index(s[i])
            if c + index < 26:
                s[i] = ualf[c + index]
            else:
                s[i] = ualf[c + index - 26]
    return ''.join(s)


def decode(text, shift):
    import string
    s = [*text]
    lalf = [*string.ascii_lowercase]
    ualf = [*string.ascii_uppercase]
    if shift <= 0:
        index = 0
    else:
        index = shift
    if index > 26:
        while index > 26:
            index -= 26

    for i in range(0, len(s)):
        if s[i] in lalf:
            c = lalf.index(s[i])
            if c - index >= 0:
                s[i] = lalf[c - index]
            else:
                s[i] = lalf[c - index + 26]
        elif s[i] in ualf:
            c = ualf.index(s[i])
            if c - index >= 0:
                s[i] = ualf[c - index]
            else:
                s[i] = ualf[c - index + 26]
    return ''.join(s)

