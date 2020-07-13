

def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logged
def sub(x, y):
    return x - y


print(sub(4, 2))
print(4, '4')
repr((4, '4'))
