def get_caller(show=False):
    import inspect
    stack = inspect.stack()
    the_class = stack[1][0].f_locals["self"].__class__.__name__
    the_method = stack[1][0].f_code.co_name
    show and print("  I was called by {}.{}()".format(str(the_class), the_method))
    return the_class, the_method


def object_get(obj, dotted_key, default=None):
    import functools
    try:
        return functools.reduce(getattr, dotted_key.split('.'), obj)
    except AttributeError:
        return default


def dict_get(dictionary, dotted_key, default=None):
    import functools
    keys = dotted_key.split('.')
    try:
        return functools.reduce(lambda d, key: d.get(key) if d else default, keys, dictionary)
    except AttributeError:
        return default
