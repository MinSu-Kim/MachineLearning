import pandas as pd

def dp_set():
    pd.reset_option("^display")
    pd.set_option('display.width', 2400)  # 출력 전체폭 너비
    pd.set_option('display.max_columns', None)
    pd.set_option("display.float_format", '{:.10f}'.format)


def printObj(*a):
    for x in a:
        if isinstance(x, str):
            print(x)
        else:
            print(type(x))
            print(x)
            print('-' * 45)
    print()