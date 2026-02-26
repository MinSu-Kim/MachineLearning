import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 2, 4]]
    df2 = pd.DataFrame(data2, index=list('ABCD'), columns=['가', '나', '다'])
    print(df2, df2.cumsum(), df2.cumsum(axis=1), sep='\n', end='\n\n')
    print(df2['가'].drop('A'), df2.drop('A', axis=0), sep='\n', end='\n\n')
    print(df2, df2.gt(2), df2.gt(2).all(),df2.gt(2).all(axis=1), sep='\n', end='\n\n')
    print(df2.corr())