import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv'
    df = pd.read_csv(DataUrl)

    '''
    Question 76
    년-월-일:시 컬럼을 pandas에서 인식할 수 있는 datetime 형태로 변경하라. 
    서울시의 제공데이터의 경우 0시가 24시로 표현된다
    '''

    df_copy = df.rename(columns={'(년-월-일:시)': 'date'})
    #pd.to_datetime(df_copy['date'], format='%Y-%m-%d:%H')

    print('\nQuestion 76',
          df_copy[df_copy['date'].str[-2:] == '24'],
          sep='\n',
          end='\n\n'
          )

    import datetime

    def change_date(x):
        hour = x.split(':')[1]
        date = x.split(':')[0]
        if hour == '24':
            hour = '00:00:00'
            finalDate = pd.to_datetime(date + ' ' + hour) + pd.Timedelta('1day')
        else:
            hour = hour + ':00:00'
            finalDate = pd.to_datetime(date + ' ' + hour)
        return finalDate


    df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change_date)

    print('\nQuestion 76',
          df.head(),
          df.info(),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 77
    일자별 영어요일 이름을 dayName 컬럼에 저장하라
    '''
    df['dayName'] = df['(년-월-일:시)'].dt.day_name()

    print('\nQuestion 77',
          df.head(10),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 78
    일자별 각 PM10등급의 빈도수를 파악하라
    '''
    pd.set_option("display.float_format", '{:.1f}'.format)

    df = df.rename(columns={'(년-월-일:시)': 'date'})

    print('\nQuestion 78',
          df[['date', 'PM10등급']].head(10),
          df.groupby([df['date'].dt.date, 'PM10등급']).size(),
          df.groupby([df['date'].dt.date, 'PM10등급']).size().unstack().fillna(0).astype('int'),
          df.groupby([df['date'].dt.date, 'PM10등급']).agg(빈도수=('PM10등급', 'count')),
          df.groupby([df['date'].dt.date, 'PM10등급'], as_index=False).size().pivot(index='date', columns='PM10등급', values='size').fillna(0),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 79
    시간이 연속적으로 존재하며 결측치가 없는지 확인하라
    '''
    print('\nQuestion 79',
          df['date'].diff().head(),
          df['date'].diff().shape,
          df['date'].diff().dropna().shape, # NaT 삭제
          df['date'].diff().dropna().unique(),
          df.head(),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 80
    오전 10시와 오후 10시(22시)의 PM10의 평균값을 각각 구하여라
    '''
    print('\nQuestion 80',
          df.head(),
          df.groupby(df['date'].dt.hour)['PM10'].mean().iloc[[10, 22]],
          sep='\n',
          end='\n\n'
    )

    '''
    Question 81
    날짜 컬럼을 index로 만들어라
    '''
    df.set_index('date', inplace=True, drop=True)

    print('\nQuestion 81',
          df.head(),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 82
    데이터를 주단위로 뽑아서 최소,최대 평균, 표준표차를 구하여라
    '''

    print(
        '\nQuestion 82',
        df.select_dtypes(include='number'),
        df.select_dtypes(include='number').resample('W').agg(['min', 'max', 'mean', 'std']),
        sep='\n',
        end='\n\n'
    )