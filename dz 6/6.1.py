def pal(s: str):
    s = s.lower().replace(' ', '')
    s2 = s
    s = list(s)
    s.reverse()
    s = ''.join(s)
    if s2==s:
        return True
    else:
        return False