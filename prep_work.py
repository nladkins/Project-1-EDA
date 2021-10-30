# this is all a mess.

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

df_labels = pd.read_pickle('data/df_labels.pickle')

df_raw_us = f.filter_data(df_raw, 1, 'country')

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

# pickle files are significantly faster to read into dfs than csv files or excel files.
# id def recommend you read these files into pandas in place of the xlsx or csv versions

dfs = [df_raw, df_labels, df_raw_us]
dfs_list = ['df_raw', 'df_labels', 'df_raw_us']
zipped = dict(zip(dfs_list, dfs))

for k, v in zipped.items():
    filename = k
    v.to_pickle(os.path.join('data', filename + '.pickle'))

# the below fcn was still working when i wrote this
# f.value_connector(1, df_raw['age'], df_labels[(f.column_connector('age', df_raw, df_labels))])

# * testing stuff for norman
import pandas as pd
import fcns as f

usdf = pd.read_pickle('data/df_raw_us.pickle')

cat_list = 'diabetes cardiovascular_disorders obesity respiratory_infections respiratory_disorders_exam ' \
           'gastrointestinal_disorders' \
           ' chronic_kidney_disease autoimmune_disease'.split()

sel = usdf[cat_list]
filt = sel.where(sel[cat_list] == 1)

# # read the data
# df_us = pd.read_pickle('df_raw_us.pickle')
#
# # slice by only the cols that correspond to comorbidities
# preexisting = df_us.loc[:, 'diabetes':'chronic_fatigue_syndrome_m']
#
# # sum the values in all of those rows, across the columns
# outs = preexisting.sum(axis=1)
# df_us['sums'] = outs
#
# # anyone who sums to 0 across these columns has 0 cormorbidities
# no_comorbs = df_us[df_us.sums == 0]  # ? len 191
# comorbs = df_us[df_us.sums != 0]  # ? len 2061
#
# # * trying another way
# preexisting = preexisting.replace(
#         {
#                 np.nan: 0
#         }
# )
#
# # anyone who has 0 for all of these columns has no comorbidities
# no_comorbs = preexisting[preexisting.isin([0]).all(axis=1)]  # ? len 191
# comorbs = preexisting[~preexisting.isin([0]).all(axis=1)]  # ? len 2061
#
# print(len(no_comorbs), len(comorbs))

cat_list = 'education income diabetes cardiovascular_disorders obesity respiratory_infections ' \
           'respiratory_disorders_exam ' \
           'gastrointestinal_disorders' \
           ' chronic_kidney_disease autoimmune_disease chronic_fatigue_syndrome_a'.split()

df_us = pd.read_pickle('data/df_raw_us.pickle')

cos_adjusted = df_us[cat_list].replace(
        {
                2: 0
        },
)

df_us.columns
idx = list(cos_adjusted.index)

df_us_filt = df_us.loc[idx]
len(df_us_filt.columns)
df_us_filt.diabetes

# ! Testing value fcn
# deprecated
# df = pd.read_pickle('data/df_raw.pickle')
# df_labels = pd.read_pickle('data/df_labels.pickle')
# # f.column_connector('diabetes', df, df_labels)
# f.column_connector('diabetes', df, df_labels)
# f.value_connector(1, df['diabetes'], f.column_connector('diabetes', df, df_labels))
