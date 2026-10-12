import pandas as pd

path_data = "data/data.csv"
path_info = "data/info.csv"

data = pd.read_csv(path_data).drop(columns=['Unnamed: 0'])
info = pd.read_csv(path_info)

data['Date'] = pd.to_datetime(data['Date'])
result = data.merge(info, on='idMeasure', how='left')

result.loc[(result['Type'] == 4) & (result['Date'] >= '2021-08-18 22:00'), ['Value1','Value2']] = None
ranges = result.groupby('Type')[['Value1','Value2']].agg(['min','max']).round(2)

print(ranges)