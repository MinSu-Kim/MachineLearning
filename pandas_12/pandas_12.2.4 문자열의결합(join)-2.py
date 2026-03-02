import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.max_rows", 8)  # 8행까지만 출력 코드
    pd.set_option("display.float_format", '{:.1f}'.format)

    # 코드 12-78. groupby 함수 심화 실습 예제 코드
    data1 = [[1, 'A', '반장', '물리001', 94],
             [1, 'A', '부반장', '화학001', 90],
             [2, 'A', '부반장', '화학002', 85],
             [2, 'A', '반원', '물리002', 95],
             [1, 'B', '부반장', '물리003', 86],
             [1, 'B', '반장', '화학003', 75],
             [1, 'B', '반원', '화학004', 80]]
    df = pd.DataFrame(data1, columns=['학년', '반', '직책', '학생코드', '점수'])
    df1 = df.set_index(['학년', '반']).copy()

    print(
        df,
        '\ngroupby 함수의 매개변수 asjndex 활용하기',
        df.groupby(['학년', '반'], as_index=False, sort=False)['점수'].mean(),
        df.groupby(['학년', '반'])['점수'].mean().reset_index(),
        df.groupby(['학년', '반'], as_index=True, sort=False)['점수'].mean(),
        df1,
        df.groupby(['학년', '반']),
        list(df.groupby(['학년', '반'])),
        sep='\n',
        end='\n\n'
    )
    [print(i) for key, i in df.groupby(['학년', '반'])]
    g = df.groupby(['학년', '반'])
    print(
        g['점수'].mean(),
        g['점수'].std(),
        g['점수'].mean() + g['점수'].std(),
        g.head(1),
        g.sample(1, random_state=0),
        sep='\n',
        end='\n\n'
    )


    # df를 복제한 df2에서 반장이 존재하는 반의 데이터만 추출
    df2 = df.copy()
    # 반장 여부를 True, False로 반환하는 반장 열을 생성
    df2['반장'] = df2['직책'].eq('반장')
    # 학년과 반으로 그룹을 나누어 반장 열에 transform 함수를 적용
    cond = df2.groupby(['학년', '반'])['반장'].transform('any')
    print(
        df2,
        df2[cond],
        df[df['직책'].eq('반장').groupby([df['학년'], df['반']]).transform('any')],
        sep='\n',
        end='\n\n'
    )
