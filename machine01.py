import pandas as pd

from sklearn.datasets import load_iris

from Function_Set import dp_set

if __name__ == "__main__":
    # 붓꽃 데이터 세트를 로딩합니다.
    iris = load_iris()

    # iris.data는 Iris 데이터 세트에서 피처(feature)만으로 된 데이터를 numpy로 가지고 있습니다.
    iris_data = iris.data

    # iris.target은 붓꽃 데이터 세트에서 레이블(결정 값) 데이터를 numpy로 가지고 있습니다.
    iris_label = iris.target
    print('iris target값:', iris_label)
    print('iris target명:', iris.target_names)

    # 붓꽃 데이터 세트를 자세히 보기 위해 DataFrame으로 변환합니다.
    iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
    iris_df['label'] = iris.target
    iris_df.head(3)

    # CSV 파일 불러오기
    dp_set()
    df = pd.read_csv('data/titanic_train.csv')
    # 불러온 데이터프레임 출력
    print(df)
