import os
import pandas as pd


class CountryAcqusition:
    universe = 'acquisition'

    def __init__(self, name, tuple_list):
        self.country_name = name
        self.year_amount_list = tuple_list  # list of tuples consists of year and amount pairs


files_list = os.listdir(f'{os.getcwd()}/data')
# create dictionary of dictionaries

d = {}
for file in files_list:
    temp_df = pd.read_excel(f"{os.getcwd()}{os.sep}data{os.sep}{file}", sheet_name='Sheet 1', header=11)
    d[str(file)+'_dict'] = temp_df.to_dict()


# list of countries with inedexes

country_tuples = d['tps00024_spreadsheet.xlsx_dict']['TIME'].items()
country_tuples_list = [element for element in country_tuples]


year_d = {}
for i in range(2008,2020):
    year_d['year_'+str(i)] = d['tps00024_spreadsheet.xlsx_dict'][str(i)]