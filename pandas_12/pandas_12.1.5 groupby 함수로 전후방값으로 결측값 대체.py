import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)
    # 코드 12-19. 그룹을 나누어 전방값으로 대체하기 실습 예제 코드

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
        df[df['보유'].notna()],
        df[df['보유'].eq(1)],
        df[df['보유'].eq(2)],
        sep='\n',
        end='\n\n'
    )

    # 코드 12-23. 그룹을 나누어 누적 합 구하기 실습 예제 코드

    data = [['2021-01-01', '김판다', 10000], ['2021-01-01', '강승주', 2000],
            ['2021-01-02', '김판다', 20000], ['2021-01-02', '강승주', 5000],
            ['2021-01-03', '강승주', 8000], ['2021-01-03', '김판다', 5000]]
    df = pd.DataFrame(data, columns=['날짜', '이름', '입금액'])

    # 각 인원의 누적 입금액을 구하자
    df['누적입금'] = df.groupby('이름')['입금액'].cumsum()
    print(
        df,
        df.sort_values('이름'),
        sep='\n',
        end='\n\n'
    )

    data1 = [['07:35', 'A', 'Log_in', float('nan')],
             ['07:36', 'A', 'Buy', 2000.0],
             ['07:37', 'A', 'Log_out', float('nan')],
             ['10:30', 'B', 'Log_in', float('nan')],
             ['11:20', 'B', 'Buy', 4000.0],
             ['11:32', 'A', 'Log_in', float('nan')],
             ['11:34', 'B', 'Buy', 3000],
             ['11:35', 'B', 'Log_out', float('nan')],
             ['11:36', 'A', 'Buy', 5000.0],
             ['11:37', 'A', 'Log_out', float('nan')]]
    df1 = pd.DataFrame(data1, columns=['시간', '회원코드', '로그', '구매금액'])
    df1['로그인'] =  df1['로그'] == 'Log_in'
    df1['그룹'] = df1.groupby('회원코드')['로그인'].cumsum()
    print(
        df1,
        df1.sort_values('회원코드'),
        df1.pivot_table('구매금액', index='회원코드', columns='그룹', aggfunc='sum'),
        sep='\n',
        end='\n\n'
    )