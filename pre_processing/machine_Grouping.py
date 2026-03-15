import pandas as pd

from Function_Set import dp_set, printObj

if __name__ == "__main__":
    dp_set()

    DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv'
    df = pd.read_csv(DataUrl)
    printObj(df.head())

