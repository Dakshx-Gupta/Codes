import pandas as pd

dic = {
    'Class': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'],
    'Pass-Percentage': [100, 100, 100, 100, 100, 100, 100, 100, 100, 98.6, 100, 99]
}

result = pd.DataFrame(dic)
print(result)
print(result.dtypes)
print('Shape of the dataframe is:')
print(result.shape)
