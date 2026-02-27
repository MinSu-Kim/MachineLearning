import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    # 코드 12-1. groupby 함수 실습 예제 코드
    data1 = {'반': ['A', 'B', 'A', 'B', 'B', 'A'],
             '점수': [88, 30, 78, 99, 62, 85]}
    df = pd.DataFrame(data1)
    df['반등수'] = df.groupby('반')['점수'].rank().astype(int)

    print(
        df,
        df['점수'].rank(),
        df.sort_values(['반', '반등수']),
        sep='\n',
        end='\n\n'
    )

    import openpyxl

    # 코드 12-6. 동명이인 엑셀 파일에서 데이터 프레임 불러오기
    url2 = 'https://github.com/panda-kim/book1/blob/main/18name.xlsx?raw=true'
    df_name = pd.read_excel(url2)
    print(
        df_name,
        df_name.shape,
        df_name.duplicated('이름').sum(),
        df_name.duplicated(['이름', '생년월일']).sum(),
        sep='\n',
        end='\n\n'
    )

    s = df_name.groupby('이름')['생년월일'].rank().astype('int').astype('str')
    df_name['이름'] = df_name['이름'] + s.replace('1', '')

    print(
        df_name,
        df_name[df_name['이름'].str.contains('한서준')],
        sep = '\n',
        end = '\n\n'
    )

    # 코드 12-14. 그룹을 나누어 행 간의 연산 실습 예제 코드
    pd.options.display.max_rows = 8  # 8행까지만 출력
    data = [['2025-01-03', '판다전자', 10000],
            ['2025-01-03', '성심당', 2000],
            ['2025-01-04', '성심당', 1600],
            ['2025-01-04', '판다전자', 12000],
            ['2025-01-05', '판다전자', 15000],
            ['2025-01-05', '성심당', 2000],
            ['2025-01-06', '판다전자', 13500],
            ['2025-01-06', '성심당', 2400]]

    df = pd.DataFrame(data, columns=['날짜', '종목', '종가'])
    print(
        df,
        df.groupby('종목')['종가'],
        sep='\n',
        end='\n\n'
    )
    df['전일종가'] = df.groupby('종목')['종가'].shift()
    df['등락'] = df.groupby('종목')['종가'].diff()
    df['등락률'] = df.groupby('종목')['종가'].pct_change()
    print(
        df,
        sep='\n',
        end='\n\n'
    )