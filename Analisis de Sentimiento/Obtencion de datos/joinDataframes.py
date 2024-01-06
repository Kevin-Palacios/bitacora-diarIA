# Joinig dataframes from Folder

import pandas as pd
import os

path = "./DataFrames"
files = os.listdir(path)

columns = ['user', 'text', 'date', 'emotion', 'sentiment', ]

sentiment_dataframe = pd.DataFrame(columns=columns)

for file in files:
    print(file)
    if file.endswith(".csv"):
        df = pd.read_csv(path+"/"+file)

        sentiment_dataframe = pd.concat([sentiment_dataframe, df], ignore_index=True)


sentiment_dataframe.to_csv("./sentiment_dataframe.csv", index=False)