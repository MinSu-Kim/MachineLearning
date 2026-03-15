import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv'
    df = pd.read_csv(DataUrl)

    '''
    Question 64
    데이터를 로드하고 각 열의 데이터 타입을 파악하라
    '''

    print('\nQuestion 64',
        df.info(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 65
    Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
    '''
    df['Yr_Mo_Dy']=pd.to_datetime(df['Yr_Mo_Dy'])

    print('\nQuestion 65',
        df.info(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 66
    Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
    '''
    print('\nQuestion 66',
        df['Yr_Mo_Dy'].dt.year.unique(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 67
    Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 
    해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
    '''
    import datetime

    def fix_year(x):
        year = x.year - 100 if x.year >= 2061 else x.year
        return pd.to_datetime(datetime.date(year, x.month, x.day))

    df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_year)

    print('\nQuestion 67',
        df['Yr_Mo_Dy'].dt.year.unique(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 68
    년도별 각 컬럼의 평균값을 구하여라
    '''
    print('\nQuestion 68',
        df.groupby(df['Yr_Mo_Dy'].dt.year).mean(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 69
    weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
    '''

    df['weekday'] = df['Yr_Mo_Dy'].dt.dayofweek
    print('\nQuestion 69',
        df['Yr_Mo_Dy'].dt.day_name(),
        df[['Yr_Mo_Dy','weekday']],
        df['weekday'],
        sep='\n',
        end='\n\n'
    )

    '''
    Question 70
    weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
    '''
    df['WeekCheck'] = df['weekday'].apply(lambda x : 1 if x >= 5 else 0)
    print(
        '\nQuestion 70',
        df[['weekday', 'WeekCheck']],
        sep='\n',
        end='\n\n'
    )

    '''
    Question 71
    년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
    '''
    print(
        '\nQuestion 71',
        df.groupby(df['Yr_Mo_Dy'].dt.month).mean(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 72
    모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
    '''
    print(df.loc[[0, 1, 27, 28, 29], :], sep='\n', end='\n\n')

    df = df.ffill().bfill()
    print(
        '\nQuestion 72',
        df.loc[[0, 27, 28, 29], :],
        sep='\n',
        end='\n\n'
    )

    '''
    Question 73
    년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
    '''
    print(df['Yr_Mo_Dy'].dt.strftime('%Y-%m-%d %H:%M:%S')) #StringFormatTime의 약자
    
    print(
        '\nQuestion 73',
        df['Yr_Mo_Dy'].dt.to_period('M'),
        df.groupby(df['Yr_Mo_Dy'].dt.to_period('M')).mean(),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 74
    RPT 컬럼의 값을 일자별 기준으로 1차 차분하라 
    0행값 -1행값 = diff()함수
    '''

    print(
        '\nQuestion 74',
        df[['Yr_Mo_Dy', 'RPT']].head(10),
        df['RPT'].diff(),
        type(df['RPT'].diff()),
        sep='\n',
        end='\n\n'
    )
    
    '''
    Question 75
    RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라
    '''

    print(
        '\nQuestion 75',
        df[['RPT', 'VAL']].head(10),
        df[ ['RPT', 'VAL'] ].rolling(7).mean().head(10),
        sep='\n',
        end='\n\n'
    )

    df.loc[:, ['RPT_rol', 'VAL_rol']] = df[ ['RPT', 'VAL'] ].rolling(7).mean().values
    print(
        '\nQuestion 75',
        df[['RPT', 'VAL', 'RPT_rol', 'VAL_rol']].head(10),
        sep='\n',
        end='\n\n'
    )