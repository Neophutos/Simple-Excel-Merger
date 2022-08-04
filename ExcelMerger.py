import os
import pandas as pd

# Enter your folder path here
# Example: 'C:\Users\neophutos\MyData'
data_file_folder = '.\ExcelFolder'

data_file = []
for file in os.listdir(data_file_folder):
    if file.endswith('.xlsx'):
        print('Loading file {0}...'.format(file))

        # Enter the name of the sheet you want to merge in sheet_name
        data_file.append(pd.read_excel(os.path.join(data_file_folder, file), sheet_name='Enter name of the sheet'))

data_file_master = pd.concat(data_file, axis=0)

# Here you can specify the output name
data_file_master.to_excel('masterfile.xlsx', index=False)
