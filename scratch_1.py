import pandas as pd
import json
from pathlib import Path
from pandas.io.json import json_normalize

# path to file

# read the file in and load using the json module
with open('facult2.json','r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

# create a dataframe
df = json_normalize(data)
print(df)
input()
df.to_csv('facult3.csv', encoding='utf-8', index=False)