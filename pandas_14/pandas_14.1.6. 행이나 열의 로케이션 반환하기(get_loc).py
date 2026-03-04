import pandas as pd

from Function_Set import dp_set

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    data = {'국어': [92, 88, 93, 95, 72],
            '영어': [82, 73, 62, 99, 92],
            '총 점': [174, 161, 155, 194, 164]}
    idx = ['김판다', '강승주', '조민영', '최진환', '박연준']
    df = pd.DataFrame(data, index=idx)

    print(
        df,
        '\nget_loc 함수로 조민영 행의 로케이션 반환하기',
        df.index.get_loc('조민영'),
        sep='\n',
        end='\n\n'
    )

    '인덱스 클래스를 데이터 프레임이나 시리즈로 변환하기(to_frame, to_series)'
    print(
        df,
        '\n인덱스 클래스를 데이터 프레임 변환하기',
        df.index.to_frame(),
        '\n인덱스 클래스를 시리즈로 변환하기',
        df.index.to_series(),
        sep='\n',
        end='\n\n'
    )

    '데이터 프레임 연결하기(join)'
    data1 = {'국어_등수': [3, 4, 2, 1, 5], '영어_등수': [3, 4, 5, 1, 2]}
    df1 = pd.DataFrame(data1, index=df.index)

    print(
        df,
        df1,
        '\nconcat 함수로 연결하기(axis=1)',
        pd.concat([df, df1], axis=1),
        '\njoin 함수로 연결하기',
        df.join(df1),
        sep='\n',
        end='\n\n'
    )
