def ft_range(stop, start=0, step=1):
    if isinstance(stop, int) and isinstance(start, int) and isinstance(step, int):
        l = []
        while start < stop:
            if start <= stop:
                l.append(start)
            else:
                return l
            start += step
        return l
    else:
        print('Value must be int')
