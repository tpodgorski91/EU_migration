import pandas as pd
import matplotlib.pyplot as plt
#redundant comment

# load
cols_name = [str(year) for year in range(2008, 2020)]
cols_name.append('TIME')

ex_file = pd.read_excel(r"D:\Maszt071\Python knownledge\migration_europe\data\tps00024_spreadsheet.xlsx",
                        sheet_name="Sheet 2",
                        header=11,
                        usecols=cols_name,
                        index_col=0)

country_s ={'Liechtenstein', 'Greece', 'North Macedonia', 'Lithuania', 'Slovakia', 'Cyprus', 'United Kingdom', 'Romania',
           'Ukraine', 'Luxembourg', 'Finland', 'Hungary', 'Denmark', 'Bulgaria', 'Montenegro', 'Portugal', 'Latvia',
           'Serbia', 'Norway', 'Poland', 'Slovenia', 'Netherlands', 'Belgium', 'Sweden', 'Estonia', 'Czechia', 'Italy',
           'France', 'Belarus', 'Armenia', 'Austria', 'Malta', 'Spain',
           'Germany (until 1990 former territory of the FRG)', 'Switzerland', 'Russia', 'Iceland', 'Albania', 'Croatia',
           'Turkey', 'Ireland'}

country_sum_d = dict.fromkeys(country_s, 0)


#transform

df_t = ex_file.T

# clear
df_t.replace(':', 0, inplace=True)

# sum all countries citizenship acquisition

for country in country_s:
    country_sum_d[country] = df_t[country].sum()

# choose top 5 country

tmp_series = pd.Series(country_sum_d).to_frame('citizenship')
top5 = tmp_series['citizenship'].nlargest(n=5)

#vizual

years_l = [str(year) for year in range(2008, 2020)]

for country in top5.index:
    plt.plot([str(year) for year in range(2008, 2020)], df_t[country], label=country)
