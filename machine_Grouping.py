import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    # Question 44 - 데이터를 로드하고 상위 5개 컬럼을 출력하라
    df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv')
    printObj(df.head())

    # Question 45 - 데이터의 각 host_name의 빈도수를 구하고 인덱스으로 정렬하여 상위 5개를 출력하라
    print(df['host_name'].value_counts().sort_index().head())
    print(df.groupby('host_name').size().head())