import pandas as pd

df = pd.read_csv("data/clean_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

print(f"Исходные данные: {len(df)} строк, {df['idMeasure'].nunique()} датчиков")

df_res = (df.set_index('Date').groupby('idMeasure').resample('1h').agg(
    
    Value1_mean=('Value1', 'mean'),
    Value1_max =('Value1', 'max'),
    Value1_min =('Value1', 'min'),
    Value2_mean=('Value2', 'mean'),
    n_records  =('Value1', 'size'),).reset_index())

print(f"После ресемпла: {len(df_res)} строк")

df_res = df_res[df_res['n_records'] > 0].copy()
print(f"После удаления пустых часов: {len(df_res)} строк")
print(f"Пропуски в Value1: {df_res['Value1_mean'].isna().mean():.2%}")
print(f"Записи на час: {df_res['n_records'].mean():.2f}")

path_for_save = "data/data_resampled_1h.csv"
print(path_for_save)