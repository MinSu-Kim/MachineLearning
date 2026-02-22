import pandas as pd

from Function_Set import dp_set

if __name__ == "__main__":
    dp_set()
    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
    df = pd.read_csv(DataUrl)
    print(df.head())

    # Question 21 - quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라
    print(df.loc[df['quantity'] == 3].head())

    # Question 22 - quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라
    print(df.loc[df['quantity'] == 3].reset_index(drop=True).head())

    # Question 23 quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라
    new_df = df[['quantity', 'item_price']].copy()
    print(new_df.head())
    new_df2 = df.loc[:, ['quantity', 'item_price']].copy()
    print(new_df2.head())

    # Question 24 item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라
    df['new_price']=df['item_price'].str.replace('$','', regex=False).astype(float)
    print(df.head())

    # Question 25 - new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라
    print(df.loc[df['new_price'] <= 5].shape[0])

    # Question 26 - item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라
    print(df.loc[df['item_name'] == 'Chicken Salad Bowl'].reset_index(drop=True))

    # Question 27 - new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
    cond = (df['new_price'] <= 9) & (df['item_name'] == 'Chicken Salad Bowl')
    print(df.loc[cond])

    # Question 28 - df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
    print(df.sort_values('new_price').reset_index(drop=True))

    # Question 29 - df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
    print(df.loc[df['item_name'].str.contains('Chips')])

    # Question 30 - df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
    print(df.iloc[:, 1::2].head())
    print(df.columns)
    print(df.loc[:, df.columns[1::2]].head())
    print(df.columns[1::2])

    # Question 31 - df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
    print(df.sort_values('new_price', ascending=False).reset_index(drop=True).head(10))

    # Question 32 - df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
    cond = (df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl' )
    print(df.loc[cond].head())

    # Question 33 - df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
    cond = (df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')
    print(df.loc[cond].drop_duplicates('item_name'))

    # Question 34 - df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
    cond = (df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')
    df_1 = df.loc[cond].drop_duplicates('item_name', keep='last')
    print(df_1)

    # Question 35 - df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
    print('new_price mean', df['new_price'].mean(), sep='\n', end='\n\n')
    print(df.loc[df['new_price'] >= df['new_price'].mean()].head())

    # Question 36 - df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
    print(sum(df['item_name']=='Izze'))
    df_2 = df['item_name'].str.replace('Izze', 'Fizzy Lizzy').copy()
    print(sum(df_2 == 'Izze'), sum(df_2 == 'Fizzy Lizzy'))

    print(sum(df['item_name'] == 'Izze'))
    df.loc[df['item_name'] == 'Izze', 'item_name'] = 'Fizzy Lizzy'
    print(df.loc[df['item_name'] == 'Izze'])
    print(df.loc[df['item_name'] == 'Fizzy Lizzy'])

