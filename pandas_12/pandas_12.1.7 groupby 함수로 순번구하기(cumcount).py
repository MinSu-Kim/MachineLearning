import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    # 코드 12-29. cumcount 함수 실습 예제 코드
    data = {'제품': ['A', 'B', 'B', 'A', 'C', 'A'],
            '판매량': [10, 20, 30, 40, 50, 60]}
    df = pd.DataFrame(data)
    df['순번'] = df.groupby('제품').cumcount()

    print(
        df,
        df.groupby('제품')['판매량'].sum(),
        df.groupby('제품')['판매량'].cumsum(),
        df.groupby('제품')['판매량'].count(),
        df.groupby('제품')['판매량'].cumcount(),
        df.pivot(index='제품', columns='순번', values='판매량'),
        sep='\n',
        end='\n\n'
    )