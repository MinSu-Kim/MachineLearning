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
        'groupby 함수로 반과 성별로 그룹을 나누어 국어 열의 평균을 구하자',
        df1.groupby(['반', '성별'])['국어'].mean(),
        'pivot_table 함수로 반과 성별로 나누어 국어 평균을 집계한 피벗 테이블을 생성',
        df1.pivot_table('국어', index=['반'], columns=['성별'], aggfunc=['mean']),
        df1.pivot_table('국어', index=['반'], columns=['성별'], aggfunc=['mean']).unstack(),
        df1.pivot_table('국어', index=['반'], columns=['성별'], aggfunc=['mean']).stack(),
        df1.pivot_table('국어', index=['반', '성별'], aggfunc=['mean']),
        df1.groupby(['반', '성별'])['국어'].agg(['max', 'min']),
        df1.groupby(['반', '성별']).agg({'영어':'min', '국어':'count'}),
        df1.groupby(['반', '성별']).agg(
            영어평균=('영어', 'mean'),
            국어평균=('국어', 'mean'),
            인원수=('국어', 'count'),
        ),
        sep='\n',
        end='\n\n'
    )