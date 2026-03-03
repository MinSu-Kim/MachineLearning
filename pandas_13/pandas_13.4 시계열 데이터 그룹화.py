import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.max_rows", 8)  # 8행까지만 출력 코드
    pd.set_option("display.float_format", '{:.1f}'.format)

    # 코드 13-27. resample 함수 실습 예제 코드
    data = {'날짜': ['2024-02-01', '2024-03-15', '2024-03-30',
                   '2024-03-31', '2024-04-02', '2024-04-05'],
            '월': ['2024-02', '2024-03', '2024-03',
                  '2024-03', '2024-04', '2024-04'],
            '금액': [1000, 2000, 3000, 4000, 5000, 6000]}
    df = pd.DataFrame(data)

    df['날짜'] = pd.to_datetime(df['날짜'])
    df['누적금액1'] = df.resample('MS', on='날짜')['금액'].cumsum()
    df['누적금액2'] = df.groupby('월')['금액'].cumsum()
    df['분기별누적'] = df.resample('QE', on='날짜')['금액'].cumsum()

    print(
        df,
        sep='\n\n',
        end='\n\n'
    )

    # 코드 13-35. resample 함수와 집계 함수 실습 예제 코드
    date = pd.date_range('2024-01-30 19:00', periods=6, freq='9h')
    data = {'날짜': date,
            '매출': [10000, 20000, 30000, 40000, 50000, 60000],
            '마진': [1000, 2000, 4000, 6000, 7000, 8000]}
    df = pd.DataFrame(data)
    print(df.info())

    print(
        df,
        '일자별 매출 합계',
        df.resample('D', on='날짜')['매출'].sum(),
        '월별 매출 합계 월의마지막일',
        df.resample('ME', on='날짜')['매출'].sum(),
        '월별 매출 합계 월의시작일',
        df.resample('MS', on='날짜')['매출'].sum(),
        '월별 매출과 마진열의 합계',
        df.resample('MS', on = '날짜')[['매출', '마진']].sum(),
        '월별 일평균 매출',
        df,
        df.resample('D', on='날짜')['매출'].sum().resample('MS').mean(),
        sep='\n\n',
        end='\n\n'
    )

    print(
        df,
        'resample함수에 agg 적용',
        df.resample('D', on='날짜').agg(
            매출합=('매출', 'sum'),
            매출건수=('매출', 'count')
        ),
        df.resample('D', on='날짜').agg(
            매출합=('매출', 'sum'),
            매출건수=('매출', 'count')
        ).resample('MS').agg(
            매출합계=('매출합', 'sum'),
            일평균_매출=('매출합', 'mean'),
            매출건수=('매출건수', 'count'),
        ),
        sep='\n\n',
        end='\n\n'
    )

