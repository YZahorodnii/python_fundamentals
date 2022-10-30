def ft_upper(obj):
    res = ''
    if isinstance(obj, str):
        for i in obj:
            if ord(i) in range(97, 123):
                res = res + chr(ord(i) - 32)
            else:
                res = res + chr(ord(i))
        return res
    else:
        print(f'You passed {type(obj)} instead of str required')
