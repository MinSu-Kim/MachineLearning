import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    pd.options.display.float_format = '{:.1f}'.format  # 소수점 첫째 자리 출력
    data = [['김판다', '남', 'A', 97, '1등', '수시'],
            ['강승주', '여', 'A', 88, '2등', '정시'],
            ['권보아', '여', 'A', 78, '3등', '정시'],
            ['조민영', '여', 'B', 64, '3등', '수시'],
            ['박상현', '남', 'B', 84, '2등', '수시'],
            ['송중기', '남', 'B', 89, '1등', '수시'],
            ['최진환', '남', 'C', 87, '3등', '정시'],
            ['장범준', '남', 'C', 92, '2등', '정시'],
            ['안지선', '여', 'C', 99, '1등', '수시']]
    col = ['이름', '성별', '반', '점수', '반등수', '비고']

    data1 = {'제품': ['A', 'B', 'A', 'B', 'B', 'A'],
             '판매량': [float('nan'), 2, 3, 4, float('nan'), 6]}

    df = pd.DataFrame(data, columns=col)
    df1 = pd.DataFrame(data1)

    print(
        df,
        df.pivot_table('점수', index=['반', '성별'], columns='비고'),
        df.pivot_table('점수', index=['반'], columns='성별', aggfunc=['mean', 'count']),
        df.pivot_table('점수', index=['반'], columns='성별', aggfunc=['mean', 'count']).unstack(),
        sep = '\n',
        end = '\n\n'
    )

    print(
        df1,
        df1.pivot_table('판매량', index='제품', aggfunc=['last']),
        df1.pivot_table('판매량', index='제품', aggfunc=['first']),
        sep = '\n',
        end = '\n\n'
    )

    print(
        df.sort_values('점수', ascending=False),
        df.sort_values('점수', ascending=False).pivot_table('이름', index=['반'], columns=['성별'], aggfunc='first'),
        sep = '\n',
        end = '\n\n'
    )

    # 11.1.7. 문자열 피벗(pivot)
    print(
        df.pivot(index='반', columns='반등수', values='이름'),
        sep='\n',
        end='\n\n'
    )

    # 코드 11-10. crosstab 함수 실습 예제 코드
    data = {'반': ['A', 'A', 'A', 'B', 'B', 'B'],
            '성별': ['남', '여', '여', '여', '남', '남']}
    df = pd.DataFrame(data)
    print(
        df,
        pd.crosstab(df['반'], df['성별']),
        sep='\n',
        end='\n\n'
    )