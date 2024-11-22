import pandas as pd

data = [
    'house_data1.csv',
    'house_data2.csv',
    'house_data3.csv',
    'house_data4.csv',
    'house_data5.csv',
    'house_data6.csv',
    'house_data7.csv',
    'house_data8.csv',
    'house_data9.csv',
    'house_data10.csv'
]

combinedData = pd.concat([pd.read_csv(file) for file in data], ignore_index=True)
combinedData = combinedData.drop_duplicates()
combinedData.to_csv('clean_house_data.csv', index=False)
print('a ok')