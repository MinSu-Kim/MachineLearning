import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    # 코드 10-40. 판다스의 문자열 함수에 정규 표현식 활용 예제 코드
    s = pd.Series(['02-222-3333', '053)333-4444', '051/555/6666', '02/777-8888'])

    print(
        s,
        s.str.replace('[)/]','-', regex=True),
        s.str.split('[)/-]', regex=True).str[0],
        s.str.contains('^02|^051'),
        sep = '\n',
        end = '\n\n'
    )

    # 코드 10-44. 정규 표현식을 활용해 문자열 추출 예제 코드
    s1 = pd.Series(['A반김판다/B반강승주', 'A반최진환/B반안지선'])
    s2 = pd.Series(['A반박연준/A반권보아', 'A반임재범'])
    s3 = pd.Series(['cat01', '02cat', 'dog01', '01cow'])
    print(s1, s2, s3, sep = '\n', end = '\n\n')
    print(
        s1.str.extract('A반([가-힣]+)/B반([가-힣]+)'),
        s2.str.extract('A반([가-힣]+)'),
        s2.str.extractall('A반([가-힣]+)'),
        s2.str.extractall('A반([가-힣]+)').unstack(),
        s2.str.extractall('A반([가-힣]+)')[0].unstack(),
        type(s2.str.extractall('A반([가-힣]+)')),
        type(s2.str.extractall('A반([가-힣]+)')[0]),
        type(s2.str.extractall('A반([가-힣]+)').unstack()),
        type(s2.str.extractall('A반([가-힣]+)')[0].unstack()),
        s3.str.extract('(cat|dog)'),
        sep='\n\n',
        end='\n\n'
    )