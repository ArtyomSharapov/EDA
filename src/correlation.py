import pandas as pd
import numpy as np

df = pd.read_csv("data/clean_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

df = (df.groupby(['idMeasure', 'Date'])
        .agg(Value1_mean=('Value1','mean'),
             spectr_name=('spectr_name','first'),
             piont_name =('piont_name','first'),
             Direction  =('Direction','first')).reset_index())

pivot = df.pivot_table(index='Date', columns='idMeasure', values='Value1_mean')
corr  = pivot.corr()

mask = np.triu(np.ones(corr.shape), k=1).astype(bool)
vals = corr.where(mask).stack()

print(f"Всего пар: {len(vals)}")
print(f"Средняя корреляция:{vals.mean():.3f}")
print(f"Медиана: {vals.median():.3f}")
print(f"Минимум: {vals.min():.3f}")
print(f"Максимум: {vals.max():.3f}")

print(f"r > 0.9: {(vals.abs()>0.9).sum():>5} ({(vals.abs()>0.9).mean():.1%})")
print(f"r > 0.7: {(vals.abs()>0.7).sum():>5} ({(vals.abs()>0.7).mean():.1%})")
print(f"r > 0.5: {(vals.abs()>0.5).sum():>5} ({(vals.abs()>0.5).mean():.1%})")
print(f"r > 0.3: {(vals.abs()>0.3).sum():>5} ({(vals.abs()>0.3).mean():.1%})")

print("сильные связи:")
top = vals.abs().sort_values(ascending=False).head(10)
for (a, b), _ in top.items():
    print(f"  {a} ↔ {b}: r = {corr.loc[a,b]:+.3f}")

df['base_spectr'] = df['spectr_name'].str.replace(r'-(V|НЧ|А)$', '', regex=True)
combo = df.groupby(['piont_name','Direction','base_spectr'])['idMeasure'].nunique()

print(f"Физических каналов: {len(combo)}")
print(f"Подканалы: {combo.mode().iloc[0]}")
print(f"Всего idMeasure: {df['idMeasure'].nunique()}")