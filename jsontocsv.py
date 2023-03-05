import pandas as pd

with open('Universitets.json', encoding='utf-8-sig') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('Universitets1.csv', encoding='utf-8', index=False)