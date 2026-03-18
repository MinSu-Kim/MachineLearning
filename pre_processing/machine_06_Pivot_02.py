import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv'
    df = pd.read_csv(DataUrl)
    printObj(df.head())

    '''
    Question 87
    데이터에서 한국 KOR 데이터만 추출하라
    '''

    print(
        '\nQuestion 87',
        df[df['Country'] == 'KOR'],
        sep='\n',
        end='\n\n'
    )

    '''
    Question 88
    한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
    aggfunc=size nan포함하고 그룹별 한번만계산, aggfunc=count nan제외 컬럼별 계산
    '''
    df_kr = df[df['Country'] == 'KOR']

    print(
        '\nQuestion 87',
        df_kr.pivot_table(index='Year', columns='Medal', aggfunc='size'),
        df_kr.pivot_table(index='Year', columns='Medal', aggfunc='size').fillna(0),
        df_kr.pivot_table(index='Year', columns='Medal', aggfunc='size', fill_value=0),
        '\n',
        df_kr.pivot_table(index='Year', columns='Medal', aggfunc='count')['Athlete'].fillna(0).astype(int),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 89
    전체 데이터에서 sport종류에 따른 성별수를 구하여라
    '''
    print(
        '\nQuestion 89',
        df.groupby(['Sport', 'Gender']).size().unstack(),
        df.pivot_table(index='Sport', columns='Gender', aggfunc='size'),
        sep='\n',
        end='\n\n'
    )

    '''
    Question 90
    전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
    '''
    print(
        '\nQuestion 90',
        df.pivot_table(index='Discipline', columns='Medal', aggfunc='size'),
        sep='\n',
        end='\n\n'
    )