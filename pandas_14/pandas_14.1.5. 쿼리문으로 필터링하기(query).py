import pandas as pd

from Function_Set import dp_set

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    data = {'국어': [92, 88, 93, 95, 72],
            '영어': [82, 73, 62, 99, 92],
            '총 점': [174, 161, 155, 194, 164]}
    idx = ['김판다', '강승주', '조민영', '최진환', '박연준']
    df = pd.DataFrame(data, index=idx)

    print(
        df,
        '국어가 90점보다 높은 데이터 필터링',
        df.query('국어 > 90'),
        sep='\n',
        end='\n\n'
    )

    n = 90
    print(
        df,
        '\n외부 변수 n으로 국어가 90점보다 높은 데이터 필터링',
        df.query('국어 > @n'),
        '\n영어에 10점을 더한 값보다 국어가 높은 데이터 필터링',
        df.query('국어 > 영어 + 10'),
        '\n국어가 80보다 크고 영어가 80보다 큰 데이터 필터링',
        df.query('(국어>80) & (영어>80)'),
        '\n열 이름에 공백이 존재하면 백틱(`) 기호를 활용',
        df.query('`총 점` > 170'),
        '\n인덱스는 index로 지정, 문자열은 다른 종류의 따옴표를 사용',
        df.query('index == "강승주"'),
        sep='\n',
        end='\n\n'
    )

