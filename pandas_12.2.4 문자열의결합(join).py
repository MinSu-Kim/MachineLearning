import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.2f}'.format)

    # 코드 12-71. 배열의 문자열을 하나로 결합하는 파이썬의 join 함수
    s = pd.Series(['A', 'BC', 'DEF'])
    print(
        s,
        '/'.join(s),
        sep='\n',
        end='\n\n'
    )

    data1 = [['김판다', 'A', '남', 95, 90], ['최진환', 'B', '남', 93, 90],
             ['조민영', 'B', '여', 88, 80], ['박연준', 'A', '남', 85, 70],
             ['강승주', 'B', '여', 78, 90], ['안지선', 'A', '여', 72, 70]]
    df = pd.DataFrame(data1, columns=['이름', '반', '성별', '국어', '영어'])

    print(
        df.sort_values('반'),
        '\n각 영어 점수에 해당하는 인원의 이름을 슬래시(/)로 묶어보자',
        df.groupby('영어').agg(학생=('이름', '/'.join)),
        '\n반별 국어 열의 최대와 최소 격차 구하기',
        df.groupby('반').agg(
            최대_최소=('국어', lambda x: x.max() - x.min())
        ),
        sep='\n',
        end='\n\n'
    )

    print(
        df.sort_values('반'),
        sep='\n',
        end='\n\n'
    )

    cond = df['성별'] == '남'
    print(
        df.sort_values('성별'),
        '\ndf에서 남 학생들의 국어 점수 평균을 집계',
        df['국어'].where(cond).mean(),
        df.groupby('반').agg(
            국어_남자_평균 = ('국어', lambda x: x.where(cond).mean()),
            국어_여자_평균 = ('국어', lambda x: x.where(~cond).mean()),
            국어_전체_평균 = ('국어', 'mean')
        ),
        sep='\n',
        end='\n\n'
    )
