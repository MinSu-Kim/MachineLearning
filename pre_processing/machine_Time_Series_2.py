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

    print('\nQuestion 64',
        df.info(),
        sep='\n',
        end='\n\n'
    )

