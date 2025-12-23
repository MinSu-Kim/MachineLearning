def add(a, b):
    return a+b

def div(a, b):
    return a/b


if __name__ == "__main__":
    print("hello python")
    print("hello pycharm")
    x = 10
    y =5

    res = add(x, y)
    print("add({}, {}) = {}\ndiv({}, {}) = {}".format(x, y, res, x, y, div(x, y)))