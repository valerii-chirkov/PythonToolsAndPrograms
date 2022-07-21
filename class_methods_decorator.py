vector_log = []


def class_log(log_lst):
    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_decorator(v))
        return cls

    def log_decorator(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return log_methods


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10

print(vector_log)
