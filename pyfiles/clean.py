# this is all a mess.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from _const import *

# %%
# read the files (pickles are faster)
df = pd.read_pickle('df_compick')
df_us = pd.read_csv('us_data_final.csv')
df_us['sum_comorbs'] = np.nan

# made the sum comorbs into dfus
idx = df.sum_comorbs.index
df_us['sum_comorbs'].loc[idx] = df['sum_comorbs']

df_us = df_us.loc[idx]
df_us['race'] = df_us['race_and_ethnicity']
del df_us['race_and_ethnicity']

# replacing these races with nans to easily and safely drop them
df_us['race'].replace({0: np.nan, 2: np.nan, 6: np.nan, 7: np.nan}, inplace=True)
df_us['sex'].replace(
        {
                2: np.nan,
                3: np.nan,
                4: np.nan
        }, inplace=True
)

df_dropped = df_us[['sex', 'race']].dropna()
print(df_dropped[['race', 'sex']])

# dropped_idx = df_dropped.index
# df_dropped = df_us.loc[dropped_idx]
# df_dropped['race']

# df_dropped.to_pickle('df_main_use_new')
df_dropped = pd.read_pickle('df_main_use_new')
# print(df_us['race'].isna().sum())
counts = df_dropped['race'].value_counts()

df_cat = df_dropped[cat_list]
corrs = df_cat.groupby('race').corr()

# set the colorbar ticks and tick labels
# cbar.set_ticks() = dividers

# nrows, ncols, iterator
a, b, c = 2, 2, 1
# noinspection PyTypeChecker
fig, axs = plt.subplots(2, 2, figsize=(16, 16), sharex=True, sharey=True)

v = df_cat['race'].value_counts()

df_list = []
# loop through for every race, get correlation vals, plot them on a heatmap
for i in df_cat['race'].unique():
    try:
        corr_df = corrs.query(str(i))
        mask = np.zeros_like(corr_df)
        mask[np.triu_indices_from(mask)] = True
        plt.subplot(a, b, c)

        sns.heatmap(
                corr_df,
                annot=True,
                cbar=True,
                cmap='magma',
                square=True,
                mask=mask,
                center=0,
                vmin=-1,
                vmax=1,
                linewidths=0.1,
                linecolor='lightgray',
        )
        # title is the race name and count
        plt.title(f'Race: {race_dict[i].title()}\nn={v[i]}')
        plt.tight_layout()
        plt.show()
        c += 1
        df_list.append(corr_df)
    except pd.core.computation.ops.UndefinedVariableError:
        continue

# adjustments to get everything on the graph right
plt.subplots_adjust(0.09, 0.12, 0.98, 0.9, 0.03, 0.08)

# colorbar location
cax = plt.axes([0.25, 0.96, 0.4, 0.025])
sm = plt.cm.ScalarMappable(cmap='magma', norm=plt.Normalize(vmin=-1, vmax=1))
plt.colorbar(sm, cax=cax, shrink=0.6, orientation='horizontal')
plt.savefig('heatmap_4plot.png', dpi=300)

dfcom = pd.read_pickle('df_compick')
gbo_sum = dfcom.groupby('race').agg(['sum']).droplevel(1, axis=1)

gbo_count = dfcom.groupby('race').agg(['count'])
gbo_graph = sns.barplot(gbo_sum.loc[[1, 3, 4, 5]])
plt.show()
del gbo_graph['sum_comorbs']

l = []

# [l.append(col[0])
#  for col in gbo.columns if col[0] not in l]
#
# for el in l:
#     gbo[(el, 'prev')] = gbo[el]['sum'] / gbo[el]['count']

# %%
# bar chart
from _const import *

df_cat = pd.read_pickle('data/pickledfiles/df_main_use_new')
fig, ax = plt.subplots(figsize=(10, 6))
df_cat['race'] = df_cat['race'].replace(race_dict)
df_cat['sex'] = df_cat['sex'].replace({
        0: 'Female',
        1: 'Male'
})

ax = sns.histplot(
        data=df_cat,
        x='race',
        hue='sex',
        # discrete=True,
        multiple='dodge',
)

plt.title('Population Breakdown by Race and Sex')
plt.legend(['Male', 'Female'])
plt.show()
# plt.savefig('demogs_by_race_gender.png', dpi=300)
# for i in ax.get_xticklabels()

idx = df_us[df_us['physical_overall'] != 5].index
phys = df_us.loc[idx]

gb = phys.groupby(['physical_overall', 'race']).agg('count')
gb = gb.reset_index()
gb['race_g'] = gb['race'].replace(
        {
                0: np.nan,
                2: np.nan,
                6: np.nan,
                7: np.nan
        }
).dropna()

# sns.histplot(x='physical_overall',stat='count',data=gb, hue='race', multiple='stack')
# plt.show()

fig, ax = plt.subplots(figsize=(12, 12))
v = df_cat['race'].value_counts()
sns.set(font_scale=0.8)
df_list = []

corr_df = corrs.query(str(1))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
# plt.subplot(a, b, c)

hot = sns.heatmap(
        corr_df,
        annot=True,
        cbar=True,
        cmap='magma',
        square=True,
        mask=mask,
        center=0,
        vmin=-1,
        vmax=1,
        linewidths=0.1,
        linecolor='lightgray',
)
# plt.colorbar()
plt.title(f'Race: {race_dict[i].title()}\nn={v[i]}')
# plt.subplots_adjust(0.25, 0.12, 0.8, 0.6)

plt.tight_layout()
plt.figure()
plt.show()

# cax = plt.axes([0.25, 0.96, 0.4, 0.025])
# sm = plt.cm.ScalarMappable(cmap='magma', norm=plt.Normalize(vmin=-1, vmax=1))

# plt.colorbar(sm, shrink=0.15, orientation='horizontal')
