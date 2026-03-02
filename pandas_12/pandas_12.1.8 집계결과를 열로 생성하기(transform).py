import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.3f}'.format)

    # 코드 12-43. 집계 결과를 열로 생성하기 실습 예제 코드
    data = {'제품': ['A', 'A', 'B', 'B', 'C', 'A'],
            '판매량': [10, 20, 20, 30, 10, 60]}
    df = pd.DataFrame(data)
    df['구매횟수'] = df.groupby('제품').transform('count')
    df['제품총판매'] = df.groupby('제품')['판매량'].transform('sum')
    df['비중'] = df['판매량'] / df['제품총판매']

    #2행 이상의 제품 제이터만 필터링
    cond = df.groupby('제품')['판매량'].transform('count') >= 2

    print(
        df,
        df[cond],
        df.groupby('제품')['판매량'].transform(lambda x: x.max() - x.min()),
        sep='\n',
        end='\n\n'
    )

    # 코드 12-51. transform 함수의 다양한 실습 예제 코드
    data1 = {'상품종류': ['스낵', '스낵', '스낵', '핸드폰', '핸드폰', '핸드폰'],
             '상품코드': ['S001', 'S002', 'S003', 'P001', 'P002', 'P003'],
             '가격': [6000, 10000, 4000, 10000, 1000000, 500000]}
    df1 = pd.DataFrame(data1)

    # 코드 12-52. 시리즈를 균등 분할해 범주화하는 lambda 함수를 생성하는 코드
    x = pd.Series([6000, 10000, 4000])
    print(x, pd.qcut(x, q=3, labels=['저가', '중가', '고가']), sep='\n', end='\n\n')

    #df1['분류'] = df1.groupby('상품종류')['가격'].transform(lambda x: pd.qcut(x, q=3, labels=['저가', '중가', '고가']))
    df1['분류'] = df1.groupby('상품종류')['가격'].transform(pd.qcut, q=3, labels=['저가', '중가', '고가'])

    print(
        df1,
        sep='\n',
        end='\n\n'
    )