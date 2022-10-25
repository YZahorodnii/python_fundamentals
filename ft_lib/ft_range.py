def ft_range(stop, start=0, step=1):
    if isinstance(stop, int) and isinstance(start, int) and isinstance(step, int):
        res = []
        while start < stop:
            if start <= stop:
                res.append(start)
            else:
                return res
            start += step
        return res
    else:
        print('Value must be int')
