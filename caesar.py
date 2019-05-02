def Caesar(str, n):
    up = ord('A')
    low = ord('a')
    s = ""
    for ch in str:
        if ch.isupper():
            s += chr(((ord(ch) - up + n) % 26) + up)
        if ch.islower():
            s += chr(((ord(ch) - low + n) % 26) + low)

    return s