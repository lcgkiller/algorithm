def runtime(f):
    def wrapper(*args, **kwargs):
        import timeit
        start = timeit.default_timer()
        f
        end = timeit.default_timer()
        print(end - start)
        return f()
    return wrapper