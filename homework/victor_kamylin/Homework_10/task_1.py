def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result
    return wrapper


@decor
def example(text):
    print(text)


example("print me")
