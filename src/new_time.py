import pandas as pd
import numpy as np

df = pd.read_csv("data/data_resampled_1h.csv")
df['Date'] = pd.to_datetime(df['Date'])

df['hour']    = df['Date'].dt.hour
df['weekday'] = df['Date'].dt.dayofweek
df['month']   = df['Date'].dt.month
df['date']    = df['Date'].dt.date

print("cуточная:")
print(df.groupby('hour')['Value1_mean'].agg(['mean','std']).round(2))

print("недельная:")
w = df.groupby('weekday')['Value1_mean'].agg(['mean','std']).round(2)
w.index = ['пн','вт','ср','чт','пт','сб','вс']
print(w)

print("месячная:")
print(df.groupby('month')['Value1_mean'].agg(['mean','std']).round(2))

daily = df.groupby('date')['Value1_mean'].mean().dropna()
x = (pd.to_datetime(daily.index) - pd.to_datetime(daily.index).min()).days.values
y = daily.values
slope, intercept = np.polyfit(x, y, 1)

print(f"тренд: {slope:.6f}\nв день = {slope*365:.3f} в год")
print(f"mean: {y.mean():.2f}")
print(f"изменение за год: {slope*365/y.mean()*100:.1f}%")