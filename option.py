import pandas as pd


def display_option(): # 디스플레이 설정
    pd.set_option('display.max_columns', None)  # 출력할 최대 열의 개수
    pd.set_option('display.max_colwidth', 30)  # 출력할 열의 너비
    pd.set_option('display.width', 600)  # 콘솔 출력 너비