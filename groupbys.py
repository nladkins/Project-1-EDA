#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('us_data_final.csv')
gbo = df.groupby('has_comorbs')
len(df.columns)
gbo['age'].agg(['mean', 'median'])
#%%
to_box = df.groupby('has_comorbs').describe()
to_box
#%%
nocos = df[df['has_comorbs'] == 0]
cos = df[df['has_comorbs'] != 0]

nocos.to_csv('df_no_comorbs_final.csv', index=False)
cos.to_csv('df_comorbs_final.csv', index=False)