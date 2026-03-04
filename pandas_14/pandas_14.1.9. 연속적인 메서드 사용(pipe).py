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

    data1 = {'국어_등수': [3, 4, 2, 1, 5], '영어_등수': [3, 4, 5, 1, 2]}
    df1 = pd.DataFrame(data1, index=df.index)

    'pipe 함수로 print 함수 적용하기'

    # print 함수를 함수 형태로 적용하기
    print(df.join(df1))

    # pipe 함수에 print 함수를 인수로 입력해 연속 메서드 형태로 적용하기
    df.join(df1).pipe(print)

    #작업을 변수 지정 없이 pipe 함수로 연속 메서드로 수행하기
    df.sort_values('총 점').pipe(lambda x: x['영어'] - x['국어']).pipe(print)
    print(df.sort_values('총 점').pipe(lambda x: x['영어'] - x['국어']))
