import numpy as np
import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    '열 이름 일괄적으로 변경하기(add_prefix, add_suffix)'
    data = [[1, 1, 8], [6, 9, 8], [2, 8, 7], [6, 9, 1]]
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])

    print(
        df,
        '\n열 이름에 접두사 \'Col\' 추가',
        df.add_prefix('Col'),
        '\n열 이름에 접미사 \'_column\' 추가',
        df.add_suffix('_column'),
        sep='\n',
        end='\n\n'
    )

    '열의 데이터를 반환한 뒤 삭제하기(pop)'
    df1 = df.copy()  # 코드 14-1의 df를 복제한 df1 준비
    print(df1, end='\n\n')

    df1['B + C'] = df1.pop('B') + df1.pop('C')
    print(df1, end='\n\n')

    '특정 위치에 열 생성하기(insert)'
    df1 = df.copy() # 코드 14-1의 df를 복제한 df1 준비

    '모든 열의 합을 맨 왼쪽에 total 열로 생성'
    df1.insert(0, 'total', df1.sum(axis=1))
    print(df1, end='\n\n')

    'insert 함수와 pop 함수를 조합해 C 열을 맨 왼쪽으로 이동'
    df1 = df.copy()
    df1.insert(0, 'C', df1.pop('C'))
    print(df1, end='\n\n')

    '열 생성하기(assign)'
    df1 = df.copy()
    df1 = df1.assign(count_val=3, total=df.sum(axis=1))
    print(df1, end='\n\n')

    '함수 적용 후 assign 함수를 사용할 때는 인수로 lambda 함수를 입력'
    df1 = df.copy()
    df1 = df1.mul(2).assign(total=lambda x: x.sum(axis=1))
    print(df1, end='\n\n')