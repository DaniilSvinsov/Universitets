import pandas as pd

with open('grades.json', encoding='utf-8-sig') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('grades.csv', encoding='utf-8', index=False)