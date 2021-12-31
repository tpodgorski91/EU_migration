import os
import pandas as pd


class CountryAcqusition:
    universe = 'acquisition'

    def __init__(self, name, tuple_list):
        self.country_name = name
        self.year_amount_list = tuple_list  # list of tuples consists of year and amount pairs


files_list = os.listdir(f'{os.getcwd()}/data')

# creates list of df rows where 0 position is country and rest of them are years in order 2008-2019

import pandas as pd
file_path = r"D:\Maszt071\Python knownledge\migration_europe\data\tps00024_spreadsheet.xlsx"
tmp_df = pd.read_excel(file_path, sheet_name="Sheet 1", header=11, usecols=[0] + [i for i in range(1, 24, 2)])
l_tmp = tmp_df.values.tolist()







# create dictionary of dictionaries

d = {}
for file in files_list:
    temp_df = pd.read_excel(f"{os.getcwd()}{os.sep}data{os.sep}{file}", sheet_name='Sheet 1', header=11)
    d[str(file)+'_dict'] = temp_df.to_dict()


country_d = d['tps00024_spreadsheet.xlsx_dict']['TIME']

year_d = {}

for i in range(2008, 2020):
    year_d['year_'+str(i)] = d['tps00024_spreadsheet.xlsx_dict'][str(i)]


def match_dicts():
    pairs_d = {}

    for key in set(list(country_d.keys()) + list(year_d['year_2008'].keys())):
        try:
            pairs_d.setdefault(key,[]).append(country_d[key])
        except KeyError:
            pass

        try:
            pairs_d.setdefault(key,[]).append(year_d['year_2008'][key])
        except KeyError:
            pass
    return pairs_d


if __name__ == '__main__':
    print(match_dicts())
