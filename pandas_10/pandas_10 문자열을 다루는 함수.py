import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    # 코드 10-1. 시리즈 각 셀에서 인덱싱과 슬라이싱 실습 예제 코드
    data = {'문자열': ['A0', 'B1', 'C2', 'D3'],
            '문자열2': ['물리01', '물리02', '화학01', 99],
            '리스트': [['물리', 1], ['물리', 2], ['화학', 1], ['화학', 2]]}
    df = pd.DataFrame(data)
    print(
        df,
        df['문자열'].str[0],
        df['문자열2'].str[:2],
        df['리스트'].str[0],
        sep='\n',
        end='\n\n'
    )

    # 코드 10-5. str.len 함수 실습 예제 코드
    s = pd.Series(['mom', 'get', 'pandas', 'level'])
    print(
        s,
        s.str.len(),
        sep='\n',
        end='\n\n'
    )

    # 코드 10-7. 문자열의 좌우 공백 제거 실습 예제 코드
    data1 = {'col1': ['  205', '12   '],
             'col2': ['00205', '12000']}
    df = pd.DataFrame(data1)
    print(
        df,
        df['col1'].str.strip(),
        df['col2'].str.strip('0'),
        df['col2'].str.lstrip('0'),
        sep='\n',
        end='\n\n'
    )

    # 코드 10-11. 문자열 분할 실습 예제 코드
    s = pd.Series(['a-001', 'b-002', 'cd-003'])
    print(
        s,
        s.str.split('-'),
        s.str.split('-', expand=True),
        s.str.split('-').str[0],
        sep = '\n',
        end = '\n\n'
    )

    data1 = {'주소': ['서울특별시 용산구 독서당로',
                    '경상남도 남해군 옥천로12길 302호',
                    '경상남도 김해시 가야로47길']}
    df = pd.DataFrame(data1)
    print(df)
    df[['광역시도명', '시군구명']] = df['주소'].str.split(' ', expand=True)[[0, 1]]

    print(
        df,
        df['주소'].str.split(' ', expand=True),
        type(df['주소'].str.split(' ', expand=True)),
        df['주소'].str.split(' ', expand=True).loc[:, [0, 1]],
        sep = '\n',
        end = '\n\n'
    )