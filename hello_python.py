def add(a, b):
    return a+b

def mul(a, b):
    return a * b


if __name__ == "__main__":
    print("hello python")
    print("hello pycharm")
    x = 10
    y =5

    res = add(x, y)
    print("add({}, {}) = {} \nmul({}, {}) = {}".format(x, y, res, x, y, mul(x,y)))