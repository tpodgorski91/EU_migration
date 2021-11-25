import os
import pandas as pd

files_list = os.listdir(f'{os.getcwd()}/data')
# create dictionary of dictionaries

d = {}
for file in files_list:
    a = pd.read_excel(f"{os.getcwd()}{os.sep}data{os.sep}{file}", sheet_name='Sheet 1', header=11)
    d[str(file)+'_dict'] = a.to_dict()


# citizenship_df = pd.read_excel(f'{os.getcwd()}{os.sep}data{os.sep}{files_list[0]}', sheet_name='Sheet 1', header=11)
# citizenship_dict = citizenship_df.to_dict()
# # for example Belgium
# country = citizenship_dict['TIME'][5]
# year_2008 = citizenship_dict['2008'][5]
#
# print(country, year_2008)
#
# EU_countries = [element for element in citizenship_dict["TIME"].values()]
# EU_countries_tuples = [element for element in citizenship_dict["TIME"].items()]
