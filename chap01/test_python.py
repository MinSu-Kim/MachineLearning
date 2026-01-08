from option import display_option as dp

def add(a, b):
    return a+b

def mul(a, b):
    return a * b

def div(a, b):
    return a/b


if __name__ == "__main__":
    dp()

    print("{} {}".format('hello python', 'hi pycharm'))
    x = 10
    y =5

    print("add({}, {}) = {}".format(x, y, add(x, y)))
    print("mul({}, {}) = {}".format(x, y, mul(x, y)))
    print("div({}, {}) = {}".format(x, y, div(x, y)))