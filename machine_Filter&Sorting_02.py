import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
    df = pd.read_csv(DataUrl)
    printObj(df.head())

    #Question 37 - df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
    print('choice_description 값이 NaN인 개수', sum(df['choice_description'].isnull()))
    print()

    # Question 38 - df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
    print(df.head())
    #df['choice_description'] = df['choice_description'].fillna('NoData')
    df.loc[df['choice_description'].isnull(), 'choice_description']='NoData'
    print(df.head())
    print('choice_description 값이 NaN인 개수', sum(df['choice_description'].isnull()))

    # Question 39 - df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
    print(df.loc[df['choice_description'].str.contains('Black')])

    # Question 40 - df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
    print(df.shape[0],
          df.loc[df['choice_description'].str.contains('Vegetables')].shape[0],
          df.loc[~df['choice_description'].str.contains('Vegetables')].shape[0],
          sep='\n\n')

    # Question 41 - df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
    #print(df.loc[df['item_name'].str[0]=='N'])
    print(df.loc[df['item_name'].str.startswith('N')])

    # Question 42 - df의 데이터 중 item_name 값의 단어갯수(공백포함)가 15개 이상인 데이터를 인덱싱하라
    print(df.loc[df['item_name'].str.len() >= 15])

    # Question 43 - df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라
    # lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
    df['new_price'] = df['item_price'].str.replace('$', '', regex=False).astype(float)
    print(df.head())
    lst = [1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]

    print(df.loc[df['new_price'].isin(lst)].shape[0])

    print(sorted(df.loc[df['new_price'].isin(lst)]['new_price'].unique()))

