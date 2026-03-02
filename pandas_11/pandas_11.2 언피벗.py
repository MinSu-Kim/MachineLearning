import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    # 코드 11-18. stack과 reset_index로 언피벗 실습 예제 코드
    pd.options.display.max_rows = 10  # 10행까지만 출력 코드
    data1 = {'1등': {'1회차': '김판다', '2회차': '박효신', '3회차': '김판다'},
             '2등': {'1회차': '권보아', '2회차': '권보아', '3회차': '박효신'},
             '3등': {'1회차': '박효신', '2회차': '강승주', '3회차': '김범수'}}
    df = pd.DataFrame(data1)

    print(
        df,
        df.stack(),
        df.stack().reset_index(),
        df.stack().reset_index().set_axis(['회차', '등수', '이름'], axis=1),
        sep='\n',
        end='\n\n'
    )

    df = df.stack().reset_index().set_axis(['회차', '등수', '이름'], axis=1).copy()

    print(
        df,
        pd.crosstab(df['이름'], df['등수']),
        sep='\n',
        end='\n\n'
    )

    # 코드 11-22. melt 함수 실습 예제 코드
    data = {'반': ['A', 'B', 'C'], '남': [10, 20, 15], '여': [30, 40, 35]}
    df = pd.DataFrame(data)
    df1 = df.set_index('반')

    print(
        df,
        df1,
        df.melt('반', value_vars=['남', '여']),
        df.melt('반', var_name='성별', value_name='인원수'),
        sep='\n',
        end='\n\n'
    )