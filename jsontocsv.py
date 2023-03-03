import pandas as pd

with open('facult1.json', encoding='cp1251') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('facult1.csv', encoding='utf-8', index=False)