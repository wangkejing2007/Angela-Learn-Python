def greeting():
    def inner(name):
        print(f'{name}你好！')
    return inner



def wrapper(func):
    def inner(logs):
        return [func(d) for d in logs]
    return inner