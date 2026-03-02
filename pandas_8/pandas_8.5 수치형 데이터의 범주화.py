import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    data = {'국어': {'가': 86, '나': 79, '다': 93, '라': 80},
            '영어': {'가': 90, '나': 10, '다': 50, '라': 95}}
    df = pd.DataFrame(data)
    print(df, end='\n\n')

    # 코드 8-30. df의 국어 점수를 0, 80, 90, 100의 구간으로 분류
    print(
        pd.cut(df['국어'], bins=[0, 80, 90, 100]),
        pd.cut(df['국어'], bins=[0, 80, 90, 100], labels=['C', 'B', 'A']),
        pd.qcut(df['영어'], q=[0, 0.25, 0.75, 1], labels=['C', 'B', 'A']),
        sep='\n', end='\n\n'
    )
