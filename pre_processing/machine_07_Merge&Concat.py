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
    df = pd.concat([df1, df2])

    print(
        '\nQuestion 87',
        df.shape,
        df1,
        df2,
        df,
        sep='\n',
        end='\n\n'
    )

    df3 = df.iloc[:2, :4]
    df4 = df.iloc[5:, 3:]
    print(
        df3,
        df4,
        sep='\n',
        end='\n\n'
    )

    '''
    Question 92
    df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
    '''
    Ans = pd.concat([df3, df4], join='inner')
    print(
        '\nQuestion 92',
        Ans,
        sep='\n',
        end='\n\n'
    )


    '''
    Question 93
    df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
    '''
    print(
        '\nQuestion 93',
        pd.concat([df3, df4], join='outer'),
        pd.concat([df3, df4], join='outer').fillna(0),
        sep='\n',
        end='\n\n'
    )

    df5 = df.T.iloc[:7, :3]
    df6 = df.T.iloc[6:, 2:5]
    print(
        'df5',
        df5,
        'df6',
        df6,
        sep='\n',
        end='\n\n'
    )

    '''
    Question 94
    df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. 
    Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
    '''
    print(
        '\nQuestion 94',
        df5.merge(df6, how='inner', on='Algeria'),
        pd.merge(df5, df6, on='Algeria', how='inner'),
        sep='\n',
        end='\n\n'
    )


    '''
    Question 95
    df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
    '''
    print(
        '\nQuestion 95',
        df5.merge(df6, how='outer', on='Algeria'),
        pd.merge(df5, df6, on='Algeria', how='outer'),
        sep='\n',
        end='\n\n'
    )