import pandas as pd

from Function_Set import dp_set

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    print(
        pd.Index(['A', 'B', 'C']),
        pd.RangeIndex(start=2, stop=8, step=1),
        sep='\n',
        end='\n\n'
    )

    idx1 = pd.Index(['A', 'B', 'C'])
    idx2 = pd.Index(['B', 'C', 'D'])
    print(idx1)
    print(idx2)
    print(idx1.append(idx2), end = '\n\n')

    '14.4. 멀티 인덱스'
    idx = pd.MultiIndex(
        levels=[['A', 'B'], ['C', 'D']],
        codes=[[0, 0, 1, 1], [0, 1, 0, 1]],
        names=['lev_0', 'lev_1']
    )

    print(
        idx,
        '\n멀티 인덱스로 시리즈 생성',
        pd.Series([1, 2, 3, 4], index=idx),
        sep = '\n',
        end = '\n\n'
    )