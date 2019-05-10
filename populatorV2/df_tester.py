import pandas as pd

df = pd.read_csv("import_files\Item.csv")

headers = df.columns

for index, row in df.iterrows():

    for header in headers:
        print(row[header])
        input()
