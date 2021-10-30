# %%
import pandas as pd
import pandas.core.computation.ops
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# region
# natively display more info in dfs in pycharm
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# endregion
# %%
df = pd.read_csv('us_data_final.csv')
gbo = df.groupby(['has_comorbs', 'income'])
# len(df.columns)
# gbo['age'].agg(['mean', 'median'])
# %%
sns.barplot(gbo['income'].agg('count'))
plt.show()
# %%
# nocos = df[df['has_comorbs'] == 0]
# cos = df[df['has_comorbs'] != 0]

# nocos.to_csv('df_no_comorbs_final.csv', index=False)
# cos.to_csv('df_comorbs_final.csv', index=False)

# %%
nocos = pd.read_csv('df_no_comorbs_final.csv')
cos = pd.read_csv('df_comorbs_final.csv')

fig, ax = plt.subplots(figsize=(10, 7))

# %%
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.boxplot(
        data=df,
        y='age',
        x='has_comorbs',
        whis=[100, 0],
        showfliers=False,

)

plt.xticks(
        [0, 1],
        ['No', 'Yes']
)

plt.yticks(
        [1, 2, 3, 4, 5, 6, 7],
        ['18-25', '26-35', '36-44', '46-55', '56-65', '66-75', '>75']
)

plt.xlabel('Has Comorbidities')
plt.ylabel('Age Bracket')
plt.title('Age Groups vs. Comorbidity Status')

# plt.show()
plt.savefig('boxplot_age_comorbs.png', dpi=300)
plt.show()

# %%
fig, ax = plt.subplots(figsize=(10, 7))
gb_income = df.groupby(['income', 'has_comorbs'])
print(gb_income.count())
# %%
# cos = pd.read_csv('df_comorbs_final.csv')
# nocos = pd.read_csv('df_no_comorbs_final.csv')

nocount = nocos.groupby('income')['has_comorbs'].count()
coun = cos.groupby('income')['has_comorbs'].count()
print(nocount, coun)

# %%
# d = d.reset_index()
dmean = d.groupby('income').mean()
g = sns.barplot(x=dmean.index, y=dmean, data=dmean, hue='has_comorbs')
g.set_xticklabels(
        labels=[]
)
# %%
import matplotlib.patches as mpatches

df['income'] = df['income'].replace(6, np.nan)
cc = df.groupby(['has_comorbs', 'income']).agg(va=('study_id', 'count'))
cc = cc.reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
h, l = ax.get_legend_handles_labels()

g = sns.barplot(x=cc.income, y=cc['va'], hue=cc['has_comorbs'])

g.set_xticklabels(['Low', 'Lower Middle', 'Middle',
                   'Upper Middle', 'High'])

blue_patch = mpatches.Patch(color='#5975a4', label='No')
red_patch = mpatches.Patch(color='#cc8963', label='Yes')
plt.legend(handles=[red_patch, blue_patch], title='Comorbidities')
plt.xlabel('Income Class')
plt.ylabel('Count')
plt.title('Comorbidities by Income Level')
plt.tight_layout()
# plt.legend()
plt.savefig('comorbs_income_level.png', dpi=300)
plt.show()

# ax.bar(height=gbo['income'].agg('count'), x=df['income'].unique())
# %%

# ! start here from future
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# region
# natively display more info in dfs in pycharm
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# endregion

# %%
# region
df = pd.read_csv('us_data_final.csv')
gbo = df.groupby(['has_comorbs', 'income'])

fig, ax = plt.subplots()

sns.stripplot(x=cc['income'], y=cc['va'], hue=cc['has_comorbs'])
# %%
sns.pointplot(x=cc['income'], y=cc['va'], hue=cc['has_comorbs'])
plt.show()
sns.lmplot(x='income', y='va', hue='has_comorbs', data=cc)
plt.show()
sns.pairplot(cc, hue='has_comorbs')
plt.show()
df_com.dropna(inplace=True)

# %%


# %%


# gb = df_com.groupby('race').agg(['count', 'sum'])
# ax = sns.histplot(data=df, x=)
# gb.plot(kind='scatter')
# plt.show()
# gb.describe()
# men = df[['education','income', 'men_health_matrix','phy_health_matrix']]
# cor = df.corr()
# ed_counts = df.groupby('education').describe()
#
# sns.histplot(ed_counts)
# plt.show()
# 0 indian
# 1 asian
# 2 polynesian
# 3 black
# 4 white
# 5 hispanic
# 6 > 1
# 7 no answer
# gb = df_com.groupby(['race_and_ethnicity','sex']).agg('count')

dfcom = pd.read_pickle('df_compick')
gbo = dfcom.groupby('race').agg(['sum', 'count', 'std'])
l = []

[l.append(col[0]) for col in gbo.columns if col[0] not in l]

for el in l:
    gbo[(el, 'prev')] = gbo[el]['sum'] / gbo[el]['count']

# %%
df = pd.read_csv('us_data_final.csv')
corr = df.corr()
print(corr)

sns.heatmap(corr)
plt.show()
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from _const import cat_list

# ! here

df = pd.read_pickle('df_compick')
df_us = pd.read_csv('us_data_final.csv')
df_us['sum_comorbs'] = np.nan

# made the sum comorbs into dfus
idx = df.sum_comorbs.index
df_us['sum_comorbs'].loc[idx] = df['sum_comorbs']
# %%
df_us = df_us.loc[idx]
df_us['race'] = df_us['race_and_ethnicity']
del df_us['race_and_ethnicity']

# %%
df_us['race'].replace({0: np.nan, 2: np.nan, 6: np.nan, 7: np.nan}, inplace=True)
df_us['race'].dropna(inplace=True)
counts = df_us['race'].value_counts()

import plotly.express as px
import plotly.offline as pyo

pyo.init_notebook_mode()
fig = pyo.plot(df_us, x='race', y='income')
fig.show()
plt.show()

df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip')
fig.show()
# %%
# * read this one instead of the csv
df_us.to_pickle('df_us_pickle')
# # %%
# gbo_race = df_us.groupby('race')
#
# corr_df = df_us.corr()
#
# fig, ax = plt.subplots()
# im = ax.imshow(corr_df)
#
# plt.show()
# %%


df_cat = df_us[cat_list]
df_cat['race'] = df_cat['race'].dropna()
corrs = df_us[cat_list].groupby('race').corr()
dividers = np.linspace(-1, 1, 6)

df_list = []
# %%
for i in df_cat['race'].unique():

    my_colors = sns.color_palette('rocket', n_colors=5)
    try:
        corr_df = corrs.query(str(i))

        # white_df = corrs.query('4')
        print(corr_df)
        mask = np.zeros_like(corr_df)
        mask[np.triu_indices_from(mask)] = True

        fig, ax = plt.subplots(figsize=(15, 12))
        # im = ax.imshow(white_df)
        sns.heatmap(
                corr_df,
                # xticklabels=corr_df.columns,
                # yticklabels=corr_df.columns,
                annot=True,
                cmap=my_colors,
                square=True,
                mask=mask,
                center=0,
                vmin=-1,
                vmax=1,
                linewidths=0.5,
                linecolor='lightgray'

        )

        colorbar = ax.collections[0].colorbar
        colorbar.set_label('Correlation')
        colorbar.set_ticks(dividers)
        colorbar.set_ticklabels(
                ['strong negative', 'weak negative', 'no correlation', 'weak positive', 'strong positive'])
        plt.title(f'Race: {race_dict[i].title()}\nn={v[i]}')
        plt.tight_layout()
        df_list.append(corr_df)
        plt.savefig(f'{race_dict[i]}_heatmap_discrete.png', dpi=300)
        plt.show()
        # plt.close()
    except pd.core.computation.ops.UndefinedVariableError:
        continue

# %%


# %%
# cmaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap',
#          'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r',
#          'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2',
#          'Pastel2_r',
#          'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples',
#          'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn',
#          'RdYlGn_r',
#          'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia',
#          'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot',
#          'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r',
#          'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r',
#          'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray',
#          'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r',
#          'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r',
#          'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet',
#          'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r',
#          'pink',
#          'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic',
#          'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b',
#          'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r',
#          'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r']

# for map in cmaps:
#     fig, ax = plt.subplots(figsize=(15, 12))
#     # im = ax.imshow(white_df)
#     sns.heatmap(
#             white_df,
#             xticklabels=white_df.columns,
#             yticklabels=white_df.columns,
#             cmap=map
#     )
#
#     plt.tight_layout(0.5)
#     plt.savefig(f'C:/users/danie/desktop/cmaps/{map}.png')
#     plt.close(fig)
v = df_cat['race'].value_counts()

corrs = df_cat.groupby('race').corr()
for i in df_cat['race'].unique():
    df = corrs.query(str(i))

    mask = np.zeros_like(df)
    mask[np.triu_indices_from(mask)] = True

    fig, ax = plt.subplots(figsize=(15, 12))
    # im = ax.imshow(white_df)
    sns.heatmap(
            df,
            annot=True,
            cmap='magma',
            square=True,
            mask=mask,
            center=0,
            vmin=-1,
            vmax=1,
            linewidths=0.1,
            linecolor='lightgray'
    )
    plt.title(f'Race: {race_dict[i].title()}\nn={v[i]}')
    plt.tight_layout()
    plt.savefig(f'{race_dict[i]}_heatmap.png', dpi=300)
# %%
from _const import *

# %%
race_df = df_us[['study_id', 'sex', 'race', 'sum_comorbs']].copy()
idx = list(race_df['race'].dropna().index)

race_df['sex'].replace(
        {
                2: np.nan,
                3: np.nan,
                4: np.nan
        }, inplace=True
)

m1 = race_df['sex'] == 0
m2 = race_df['sex'] == 1

idx2 = list(race_df[m1 | m2].index)

set1 = set(idx)
set2 = set(idx2)
combidx = list(set2 - set1) + idx
len(combidx)
racenew = race_df.loc[combidx]
racenew
# %%
counts = racenew.groupby(['race', 'sex']).agg('count')

# %%
race_df['sex'].replace(
        {
                2: np.nan,
                3: np.nan,
                4: np.nan
        }, inplace=True
)

race_df['sex'].dropna(inplace=True)
print(race_df.sex.value_counts())
race_df = race_df.loc[idx]
race_df
# %%
race_df['n'] = race_df.groupby('race').agg('count')
# %%
race_df['pct'] = race_df['n'] / race_df['n'].sum()
# race_df.rename(index=race_rename, inplace=True)
# %%


fig = sns.catplot(
        x=race_df.index,
        y='n',
        data=race_df
)

# fig.set(xticklabels=['Asian', 'Black', 'White', 'Hispanic'])
plt.show()
# %%
df_us = pd.read_pickle('df_us_pickle')
gbo_race = df_us.groupby('race')
corr_df = df_us.corr()
gbo_race[cat_list]
df_cat = df_us[cat_list]

df_cat['race'].dropna()

# %%
df = pd.read_csv('us_data_final.csv')
# ax = sns.boxplot(
#         data=df,
#         y='age',
#         x='has_comorbs'
# )
sns.histplot(

        data=df_us,
        x='race',
        y='income',
        # bins=30,
        # pthresh=0.5,
        # pmax=1,
        # jitter=
        hue='has_comorbs',
        stat='frequency',
        discrete=True,
        # common_norm=True,
        # cumulative=True,
        shrink=0.5)
plt.show()
# %%
fig, ax = plt.subplots(figsize=(12, 10))
ax1 = sns.catplot(
        x='income',
        y='race',
        hue='age',
        row='has_comorbs',
        orient='h',
        data=df_us, jitter=0.123, alpha=0.2
)

ax2 = sns.catplot(
        x='income',
        y='race',
        hue='age',
        row='has_comorbs',
        orient='h',
        data=df_us, jitter=0.123, alpha=0.2
)

[ax1, ax2]
plt.show()

# %%
