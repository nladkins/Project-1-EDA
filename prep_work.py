# %%

import pandas as pd
import seaborn as sns
import os
import fcns as f

fp = r'data/sources'

# df_raw = pd.read_excel(
#         os.path.join(fp, 'manuscript_raw_data.xlsx')
# )
#
# df_labels = pd.read_excel(
#         os.path.join(fp, 'labels_for_manuscript_raw_data.xlsx')
# )
df_raw = pd.read_pickle('data/df_raw.pickle')

df_labels = pd.read_pickle('data/df_labels.pickle'
)


# df_raw_us = f.filter_data(df_raw, 1, 'country')

# %%

# testing function
# print(f.filter_data(7, 'age', df_raw))
# f.value_connector(1, df_raw['age'], df_labels[(f.column_connector('age'))])
#
# connected = {}
#
# # make dict where k:v is raw_col:label_col
# for col in df_raw.columns:
#     connected[col] = f.column_connector(col)
#
# # make a df from the dict, then save to excel
# k = list(connected.keys())
# v = list(connected.values())
#
# d = pd.DataFrame.from_dict(connected.items())
# d.to_excel('column_lookups.xlsx')
# ! possible corr between obesity and fitness_health
# %%

# pickle files are significantly faster to read into dfs than csv files or excel files.
# id def recommend you read these files into pandas in place of the xlsx or csv versions

dfs = [df_raw, df_labels, df_raw_us]
dfs_list = ['df_raw', 'df_labels', 'df_raw_us']
zipped = dict(zip(dfs_list, dfs))

for k, v in zipped.items():
    filename = k
    v.to_pickle(os.path.join('data', filename + '.pickle'))

# %%
f.value_connector(1, df_raw['age'], df_labels[(f.column_connector('age', df_raw, df_labels))])