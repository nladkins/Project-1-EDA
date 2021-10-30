# this is all a mess.
# was using this for significance tests but it failed and im out of time

import pandas as pd
import numpy as np
import scipy.stats as st

df_raw = pd.read_excel('data/sources/manuscript_raw_data.xlsx')
df_raw = df_raw[df_raw['country'] == 1]
df_raw = df_raw[df_raw['sex'] < 2]
df_raw['race'] = df_raw['race_and_ethnicity']
del df_raw['race_and_ethnicity']
df_raw.head()
len(df_raw)
# df_raw = df_raw[df_raw['sex'] < 2]
# data from
# https://www.census.gov/quickfacts/fact/table/US/PST045219

pop_stats = {
        4.0: 0.763,
        1.0: 0.059,
        5.0: 0.185,
        3.0: 0.134
}

cat_list = ['study_id',
            'age',
            'race',
            'sex',
            'education',
            'income',
            # 'has_comorbs',
            # 'sum_comorbs',
            'essential',
            'total_interaction',
            'social_interaction',
            'more_time_household',
            'after_covid_interaction',
            'hobbies___1',
            'physical_overall',
            'mental_overall',
            'socio_emotional_overall',
            'physical_activities',
            'covid_exercise',
            'mental_health',
            'phy_health_matrix',
            'men_health_matrix',
            'time_spent_with_family',
            'time_spent_working',
            'time_spent_on_hobbies',
            'contributed']

df_raw.head()

df_raw['race'] = df_raw['race'].replace(
        {
                0: np.nan,
                2: np.nan,
                6: np.nan,
                7: np.nan
        }
).dropna()

gb_race = df_raw[cat_list].groupby('race').describe()

# multiindexed, so dripping it
gb_race = gb_race.reset_index().droplevel(level=1, axis=1)

# calc pct by race
vals = df_raw['race'].value_counts()
race_df = pd.DataFrame(vals)
race_df['pct'] = race_df['race'] / sum(race_df.race)
vals['pct'] = race_df['race'] / sum(race_df.race)
race_df = race_df.reset_index()
race_df.columns = ['code', 'race', 'pct']
race_df = race_df[['code', 'pct']]
race_df

from sklearn import preprocessing

exp = list(pop_stats.values())
# obs_norm = preprocessing.normalize(race_df['pct'])
# exp_norm = preprocessing.normalize(exp)
# dof = 3
chisq = st.chisquare([0.724530, 0.194362, 0.068249, 0.012859], [0.763, 0.134, 0.059, 0.185], ddof=3)

# race_freq = gb_race['count'] / gb_race[('study_id', 'count')])
# print(race_freq)
