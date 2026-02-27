import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    # 코드 12-18. 그룹을 나누어 결측값 대체하기 실습 예제 코드
    import pandas as pd

    data1 = [['2025-01-03', '판다전자', 10000, float('nan')],
             ['2025-01-03', '성심당', 2000, float('nan')],
             ['2025-01-04', '성심당', 1600, 1],
             ['2025-01-04', '판다전자', 12000, float('nan')],
             ['2025-01-05', '판다전자', 15000, 2],
             ['2025-01-05', '성심당', 2000, float('nan')],
             ['2025-01-06', '판다전자', 13500, float('nan')],
             ['2025-01-06', '성심당', 2400, float('nan')]]

    df = pd.DataFrame(data1, columns=['날짜', '종목', '종가', '구매'])
    df['보유']  = df.groupby('종목')['구매'].ffill()

    print(
        df,
        df[df['보유'].eq(1)],
        df[df['보유'].eq(2)],
        sep='\n',
        end='\n\n'
    )