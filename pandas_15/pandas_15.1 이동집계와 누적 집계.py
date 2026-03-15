import pandas as pd
import numpy as np

from Function_Set import dp_set

if __name__ == "__main__":
    dp_set()
    pd.set_option("display.float_format", '{:.1f}'.format)

    s = pd.Series([1, 2, 3, 4, 5])
    df = s.to_frame()
    df['rolling(2)'] = s.rolling(2).sum()
    df['rolling(3)'] = s.rolling(3).sum()
    df['rolling(3) period=1'] = s.rolling(3, min_periods=1).sum()
    df['rolling(3) center'] = s.rolling(3, center=True).sum()

    print(
        df,
        sep='\n',
        end='\n\n'
    )
