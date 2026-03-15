import pandas as pd
import numpy as np

from Function_Set import dp_set

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    idx1 = pd.MultiIndex.from_product([['A반', 'B반'], ['국어', '영어']])
    cols1 = pd.MultiIndex.from_product(
        [['2024년', '2025년'], ['전반기', '후반기'], ['1차', '2차', '3차', '4차']]
    )

    np.random.seed(0)  # 난수 고정
    data = np.random.randint(60, 100, (4, 16))
    df = pd.DataFrame(data, index=idx1, columns=cols1)


    print(
        df,
        '\n멀티 인덱스의 인덱싱은 튜플을 입력',
        '\n2024년 전반기 1차 성적 추출',
        df[('2024년', '전반기', '1차')],
        '\n2024년 데이터만 인덱싱',
        df['2024년'],
        '\niloc 인덱서로 첫 번째, 세 번째, 네 번째 열 인덱싱',
        df.iloc[:, [0, 2, 3]],
        sep='\n',
        end='\n\n'
    )
