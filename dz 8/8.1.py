spisok = list(map(int, input().split(' ')))

def _max(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        m = _max(arr[1:])
        if m > arr[0]:
            return m
        else:
            return arr[0]

print(_max(spisok))