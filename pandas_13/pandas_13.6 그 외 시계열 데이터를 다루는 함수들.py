import numpy as np
import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    # 실습을 위해 코드 13-51 다시 실행하기
    idx = pd.date_range('2023-11-03', periods=6, freq='43D 9h 10min 13s')
    s1 = pd.Series(idx)
    s2 = pd.Series([10, 20, 30, 40, 50, 60], index=idx)

    # print(
    #     s1,
    #     s1.dt.tz_localize('Asia/Seoul'),
    #     s1.dt.tz_localize('Asia/Seoul').dt.tz_convert('EST'),
    #     '시간 간격 생성하기(DateOffset)',
    #     s1 - pd.Timedelta('14h'),
    #     '3개월 후의 datetime으로 변환하기',
    #     s1 + pd.DateOffset(months=3),
    #     sep='\n',
    #     end='\n\n'
    # )

    # 실습을 위해 코드 13-43 다시 실행하기
    date = pd.date_range('2024-01-30 19:00', periods=6, freq='9h')
    data1 = {'날짜': date,
             '제품': ['A', 'B', 'A', 'A', 'B', 'A'],
             '매출': [10000, 20000, 30000, 40000, 50000, 60000]}
    df1 = pd.DataFrame(data1)

    'Grouper 함수를 이용해 시계열 그루퍼를 생성해 집계하기'

    # print(
    #     df1,
    #     df1.groupby(['제품', pd.Grouper(key='날짜', freq='D')])['매출'].sum(),
    #     df1.groupby('제품').resample(rule='D', on='날짜')['매출'].sum(),
    #     df1.groupby(['제품', pd.Grouper(key='날짜', freq='D')])['매출'].cumsum(),
    #     sep='\n',
    #     end='\n\n'
    # )


    # 코드 13-69. 2024-08-09부터 광복절을 제외한 8개의 영업일을 배열로 생성
    holidays = ['2024-08-15']
    weekmask = 'Mon Tue Wed Thu Fri Sat'

    # print(
    #     '2024-08-09부터 8개의 영업일을 배열로 생성(date_range)',
    #     pd.date_range('2024-08-09', periods=8, freq='B'),
    #     '2024-08-09부터 광복절을 제외한 8개의 영업일을 배열로 생성',
    #     pd.bdate_range('2024-08-09', periods=8, freq='C', holidays=holidays),
    #     '토요일을 포함한 8개의 영업일을 배열로 생성',
    #     pd.bdate_range('2024-08-09', periods=8, freq='C', holidays=holidays, weekmask=weekmask),
    #     sep='\n',
    #     end='\n\n'
    # )

    # 코드 13-71. 업샘플링 실습 예제 코드
    idx1 = pd.to_datetime(['2024-08-14 09', '2024-08-14 11', '2024-08-19 09'])
    s1 = pd.Series([10, 20, 50], index=idx1)

    # print(
    #     s1,
    #     '\n일자별 구매량 집계하기',
    #     s1.resample('D').sum(),
    #     '\n데이터가 없는 구간 NaN 생성',
    #     s1.resample('D').sum(min_count=1),
    #     '\n일자별 구매량의 누적 합으로 일자별 보유량 구하기',
    #     s1.resample('D').sum().cumsum(),
    #     sep='\n',
    #     end='\n\n'
    # )

    idx2 = pd.to_datetime(['2024-08-14', '2024-08-16', '2024-08-19'])
    s2 = pd.Series([10, 20, 50], index=idx2)

    # print(
    #     s2,
    #     '\nasfreq 함수로 업샘플링 수행',
    #     s2.asfreq('D'),
    #     '\nasfreq 함수로 업샘플링 수행 NaN을 0으로 치환',
    #     s2.asfreq('D', fill_value=0),
    #     '\n일자별 구매량의 누적 합으로 일자별 보유량 구하기',
    #     s2.asfreq('D', fill_value=0).cumsum(),
    #     '2일 간격으로 데이터 필터링',
    #     s2.asfreq('2D'),
    #     sep='\n',
    #     end='\n\n'
    # )

    # 생성한 시계열 배열과 reindex 함수로 업샘플링 수행
    holidays = ['2024-08-15']
    date = pd.bdate_range('2024-08-13', end='2024-08-21', freq='C', holidays=holidays)

    print(
        s2,
        '\n생성한 시계열 배열과 reindex 함수로 업샘플링 수행',
        s2.reindex(date),
        sep='\n',
        end='\n\n'
    )