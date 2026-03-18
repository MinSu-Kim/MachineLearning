import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv'
    df = pd.read_csv(DataUrl, index_col=0)
    printObj(df.head())

    df1 = df.iloc[:4, :]
    df2 = df.iloc[4:, :]

    '''
    Question 91
    df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
    '''

    print(
        '\nQuestion 87',
        df.shape,
        df1,
        df2,
        sep='\n',
        end='\n\n'
    )