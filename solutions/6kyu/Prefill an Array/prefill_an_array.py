def prefill(n, v='undefined'):
    if n is None:
        raise TypeError("None is invalid")
    try:
        n = int(n)
    except ValueError:
        raise TypeError(n + " is invalid")
    return [v] * n
