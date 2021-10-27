#%%
import pandas as pd


# cos = pd.read_csv('preexisting_us.csv')

# nocos = pd.read_csv('nonexisting_us.csv')

dfus = pd.read_pickle('data/df_raw_us.pickle')

cat_list = 'education income diabetes cardiovascular_disorders obesity respiratory_infections ' \
           'respiratory_disorders_exam ' \
           'gastrointestinal_disorders' \
           ' chronic_kidney_disease autoimmune_disease'.split()

repl_list = 'diabetes cardiovascular_disorders obesity respiratory_infections ' \
           'respiratory_disorders_exam ' \
           'gastrointestinal_disorders' \
           ' chronic_kidney_disease autoimmune_disease'.split()

dfus[repl_list] = dfus[repl_list][2:].replace(2,0)


# * i didnt mean to do this and the result it returns surprised me but i like it
# * gives number of occurrences of each unique row combo
#%%
df_replace = dfus[repl_list]
df_replace = df_replace.dropna()

df_replace['sum_comorbs'] = df_replace.sum(axis=1)

no_comorbs_idx = list(df_replace[df_replace['sum_comorbs'] == 0].index)
comorbs_idx = list(df_replace[df_replace['sum_comorbs'] != 0].index)

df_no_comorbs = dfus.loc[no_comorbs_idx]
df_comorbs = dfus.loc[comorbs_idx]

#%%

df_comorbs.to_csv('df_comorbs_final.csv', index=False)
df_no_comorbs.to_csv('df_no_comorbs_final.csv', index=False)
#%%
dfco = pd.read_csv('df_comorbs_final.csv')
dfnoco = pd.read_csv('df_no_comorbs_final.csv')

#%%
df_replace['has_comorbs'] = 9
df_replace['has_comorbs'].loc[no_comorbs_idx] = 0
df_replace['has_comorbs'].loc[comorbs_idx] = 1
df_replace.to_csv('us_data_final.csv', index=False)

#%%
