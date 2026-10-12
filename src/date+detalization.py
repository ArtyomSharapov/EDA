import pandas as pd

path = "data/data.csv"
columns = pd.read_csv(path)
columns["Date"] = pd.to_datetime(columns["Date"])

print("первая дата:",columns['Date'].min())
print("последняя дата:",columns['Date'].max())
print("период:",columns['Date'].max() - columns['Date'].min())

step = columns.groupby('idMeasure')['Date'].diff()
step = step[step > pd.Timedelta(0)] 

print(step.value_counts().head(10))
print("детализация:", step.mode().iloc[0])