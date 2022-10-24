
def ft_range(stop, start=0, step=1):
    l = []
    while start < stop:
        if start <= stop:
            l.append(start)
        else:
            l = []
        start += step
    print(l)

