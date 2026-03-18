import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv'
    df = pd.read_csv(DataUrl)
    printObj(df.head())
    '''
    Question 83
    Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
    '''

    df.drop('Indicator', axis=1, inplace=True)
    print(
        df['First Tooltip'].map(lambda x: x.split(" ")[0]),
        df['First Tooltip'].map(lambda x: x.split(" ")[1]),
        df['First Tooltip'].map(lambda x: float(x.split(" ")[0])),
    )

    df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split("[")[0]))

    print('\nQuestion 83',
          df.head(),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 84
    년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
    '''
    print('\nQuestion 84',
          df.info(),
          df[ (df['Period'] >= 2015) & (df['Dim1'] == 'Both sexes') ],
          sep='\n',
          end='\n\n'
    )

    '''
    Question 85
    84번 문제에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
    '''
    df_sample = df[(df['Period'] >= 2015) & (df['Dim1'] == 'Both sexes')]
    print('\nQuestion 84',
          df_sample.head(),
          df_sample.groupby(['Location', 'Period']).size(),
          df_sample.pivot(index='Location', columns='Period', values='First Tooltip'),
          sep='\n',
          end='\n\n'
    )

    '''
    Question 86
    Dim1에 따른 년도별 사망비율의 평균을 구하라
    '''
    print('\nQuestion 84',
          df.groupby(['Dim1', 'Period']).size(),
          df.pivot_table(index='Dim1', columns='Period', values='First Tooltip', aggfunc='mean'),
          sep='\n',
          end='\n\n'
    )