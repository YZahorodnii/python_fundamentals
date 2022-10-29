obj = 'aBC4d'

def ft_title(obj):
    j = 0
    s = ''
    start = True
    i = 1
    if isinstance(obj, str):
        for item in obj:
            if ord(item) in range(97, 123) and start:
                j = ord(item) - 32
                s = s + chr(j)
                # print(ord(item))
                start = False
            elif ord(item) in range(65, 91):
                j = ord(item) + 32
                s = s + chr(j)
                start = True
            elif not start and ord(item) in range(97, 123):
                j = ord(item)
                s = s + chr(j)
            else:
                j = ord(item)
                s = s + chr(j)
        print(s)

ft_title(obj)
