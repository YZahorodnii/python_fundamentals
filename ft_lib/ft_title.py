def ft_title(obj):
    res = ""
    start = False
    if isinstance(obj, str):
        for item in obj:
            if ord(item) not in range(97, 123) and ord(item) not in range(65, 91):
                res = res + chr(ord(item))
                start = False
            else:
                if (ord(item) in range(97, 123) or ord(item) in range(65, 91)) and not start:
                    if ord(item) in range(97, 123):
                        res = res + chr(ord(item) - 32)
                    else:
                        res = res + chr(ord(item))

                    start = True
                elif (ord(item) in range(97, 123) or ord(item) in range(65, 91)) and start:
                    if ord(item) in range(97, 123):
                        res = res + chr(ord(item))
                    else:
                        res = res + chr(ord(item) + 32)

    return res
