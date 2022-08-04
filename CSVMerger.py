import os
import pandas as pd

# Enter your folder path here
# Example: 'C:\Users\neophutos\MyData'
data_file_folder = '.\csvFolder'

data_file = []
for file in os.listdir(data_file_folder):
    if file.endswith('.csv'):
        print('Loading file {0}...'.format(file))

        # Enter the type of encoding
        data_file.append(pd.read_csv(os.path.join(data_file_folder, file), encoding=''))

data_file_master = pd.concat(data_file, axis=0)

# Here you can specify the output name
data_file_master.to_csv('masterfile.csv', index=False)
