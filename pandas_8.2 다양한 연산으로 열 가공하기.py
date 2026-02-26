import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    # 코드 8-1. 연산으로 열 가공하기 실습 예제 코드
    data1 = [['A', 0.1, 50, 0, 5], ['B', 0.25, 400, 40, 99],
             ['C', 0.35, 100, 10, 36], ['D', 0.3, 300, 4, 91]]
    df1 = pd.DataFrame(data1, columns=['선수', '적중률', '타수', '홈런', '안타'])
    print(df1)
    df1['타율'] = df1['안타'] / df1['타수']
    print(df1, end='\n\n')

    # 코드 8-3. 통계 함수를 사용해 열 가공하기 실습 예제 코드
    data2 = [[10, 0, 20], [30, 30, 40], [0, 20, 10], [30, 10, 10]]
    idx = ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04']
    df2 = pd.DataFrame(data2, index=idx, columns=['A품목', 'B품목', 'C품목'])
    print(df2)
    df2['일판매량'] = df2.sum(axis=1)
    df2['누적판매'] = df2['일판매량'].cumsum()
    print(df2, end='\n\n')

    # 코드 8-7. 순위 매기기 실습 예제 코드
    pd.options.display.float_format = None  # 소수점 출력 옵션 리셋
    s = pd.Series([90, 70, 80, 60], index=list('ABCD'))
    print(s)
    print(s.rank(ascending=False), '\n', s.rank(ascending=False).astype(int), '\n', s.rank(pct=True), end='\n\n')

    # 코드 8-11. 동점자 처리 실습 예제 코드
    data = [['김판다', 82, 17], ['권보아', 95, 17], ['강승주', 95, 18],
            ['안지선', 72, 18], ['조민영', 72, 19], ['최진환', 95, 19]]
    df = pd.DataFrame(data, columns=['이름', '점수', '나이'])

    # 코드 8-12. 다양한 방법으로 동점자 처리하기
    df['average'] = df['점수'].rank(ascending=False)
    df['min'] = df['점수'].rank(ascending=False, method='min')
    df['max'] = df['점수'].rank(ascending=False, method='max')
    df['first'] = df['점수'].rank(ascending=False, method='first')
    df['dense'] = df['점수'].rank(ascending=False, method='dense')
    print(df)