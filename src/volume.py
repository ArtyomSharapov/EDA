import pandas as pd

path_data = "data/data.csv"
path_info = "data/info.csv"

data = pd.read_csv(path_data).drop(columns=['Unnamed: 0'])
info = pd.read_csv(path_info)

data['Date'] = pd.to_datetime(data['Date'])
df = data.merge(info, on='idMeasure', how='left')

vol = df.groupby('idMeasure').size()

print("всего датчиков:", vol.size)
print("разница:", vol.max() / vol.min())

print("меньше всего записей:", vol.idxmin(), "—", vol.min(), "записей")
print("больше всего записей:", vol.idxmax(), "—", vol.max(), "записей")