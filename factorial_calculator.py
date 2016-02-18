f  = 1

def calc_f(n, v=1):
    if n <= 1:
        return v
    else:
        return calc_f(n - 1, v * n)
