import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.2f}'.format)

    # 코드 12-60. groupby 함수로 집계하기 실습 예제 코드
    data1 = {'반': ['A', 'B', 'A', 'B', 'B', 'A'],
             '점수': [88, 30, 78, 99, 62, 85]}
    df = pd.DataFrame(data1)

    print(
        df,
        df.groupby('반')['점수'].mean(),
        sep='\n',
        end='\n\n'
    )

    # 코드 12-62. groupby와 pivot_table 비교 실습 예제 코드
    data1 = [['김판다', 'A', '남', 95, 90], ['최진환', 'B', '남', 93, 90],
             ['조민영', 'B', '여', 88, 80], ['박연준', 'A', '남', 85, 70],
             ['강승주', 'B', '여', 78, 90], ['안지선', 'A', '여', 72, 70]]
    df1 = pd.DataFrame(data1, columns=['이름', '반', '성별', '국어', '영어'])
    print(
        df1,

        sep='\n',
        end='\n\n'
    )