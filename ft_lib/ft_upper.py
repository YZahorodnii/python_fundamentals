
def ft_upper(obj):
    l = ''
    if isinstance(obj, str):
        for i in obj:
            if ord(i) in range(97, 123):
                j = ord(i) - 32
                l = l + chr(j)
            else:
                j = ord(i)
                l = l + chr(j)
        return l
    else:
        print(f'You passed {type(obj)} instead of str required')
