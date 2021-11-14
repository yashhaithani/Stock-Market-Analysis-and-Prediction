import pandas as pd


data = pd.read_csv("file.csv")
data = data.drop(["Trades"], axis=1)
data = data.dropna()

data.to_csv("file_NEW.csv", index=False)
