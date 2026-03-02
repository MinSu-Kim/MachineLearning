import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.max_rows", 8)  # 8행까지만 출력 코드
    pd.set_option("display.float_format", '{:.1f}'.format)

    # 코드 13-1. to_datetime 함수 실습 예제 코드

    data = ['2023-01-01', '2023-02-02', '2023-03-02', '2023-04-10', '2023-05-31']
    s = pd.Series(data)
    s1 = pd.Series(['2022-01-03', '김판다'])

    print(
        s,
        pd.to_datetime(s),
        s1,
        pd.to_datetime(s1, errors = 'coerce'),
        sep='\n\n',
        end='\n\n'
    )

    s2 = pd.to_datetime(s)
    df = pd.DataFrame(s2, columns=['day'])
    df['day+2'] = s2 + pd.Timedelta('2 day')
    df['Quarter'] = s2.dt.to_period(freq='Q')

    print(
        s2,
        s2 + pd.Timedelta('2 day'),
        s2.dt.to_period(freq='Q'),
        df,
        sep='\n\n',
        end='\n\n'
    )

    # 코드 13-6. DatetimeIndex의 인덱싱과 슬라이싱 실습 예제 코드
    date = ['2025-12-31 00:30:10', '2026-01-10 16:40:10', '2026-01-10 18:50:10',
            '2026-02-01 07:00:10', '2026-02-12 16:40:10', '2026-04-01 19:20:10']
    s = pd.Series([10, 20, 30, 40, 50, 60], index=pd.to_datetime(date))
    print(
        'DatetimeIndex의 인덱싱과 슬라이싱',
        s,
        s.info(),
        s.loc['2026'],
        s.loc['2026Q1'],
        '2026년 1월에서 2026년 2월의 데이터 슬라이싱',
        s.loc['2026/1':'2026/2'],
        '2026년 1월 10일 18시 이후의 데이터 슬라이싱',
        s.loc['2026/1/10 18':],
        '특정 시간대의 데이터 추출하기(at_time, between_time)',
        s.at_time('16:40:10'),
        '날짜와 관계없이 07시부터 18시까지의 데이터만 추출',
        s.between_time('07', '18'),
        '2025-01-03부터 2025-01-14까지 모든 날짜를 배열로 생성',
        pd.date_range('2025-01-03', '2025-01-14'),
        '2025-01-03부터 4개의 날짜를 배열로 생성',
        pd.date_range('2025-01-03', periods=4),
        sep='\n\n',
        end='\n\n'
    )