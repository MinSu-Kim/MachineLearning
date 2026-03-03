import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.max_rows", 8)  # 8행까지만 출력 코드
    pd.set_option("display.float_format", '{:.1f}'.format)

    # 코드 13-51. 다양한 시계열 데이터 추출 실습 예제 코드
    idx = pd.date_range('2023-11-03', periods=6, freq='43D 9H 10T 13S')
    s1 = pd.Series(idx)
    s2 = pd.Series([10, 20, 30, 40, 50, 60], index=idx)

    print(
        s1,
        s1.dt.year,     # 연도
        s1.dt.quarter,  # 분기
        s1.dt.month,    # 월
        s1.dt.day,      # 일
        s1.dt.hour,     # 시각
        s1.dt.minute,   # 분
        s1.dt.second,   # 초
        s1.dt.normalize(),
        sep='\n',
        end='\n\n'
    )

    print(
        s1,
        s2.index.year,      # 연도
        s2.index.quarter,   # 분기
        s2.index.month,     # 월
        s2.index.day,       # 일
        s2.index.hour,      # 시각
        s2.index.minute,    # 분
        s2.index.second,    # 초
        sep='\n',
        end='\n\n'
    )

    print(
        '문자열로 변환하기(strftime)',
        s1,
        s1.dt.strftime('%m/%d/%Y'),
        sep='\n',
        end='\n\n'
    )

    tmp = s2.resample('Q').sum()
    # tmp.set_axis(tmp.index.to_period('Q'))

    print(
        'period 자료형으로 변환하기(to_period)',
        s2,
        s2.resample('Q').sum(),
        s2.resample('Q').sum().set_axis(tmp.index.to_period('Q')),
        sep='\n',
        end='\n\n'
    )