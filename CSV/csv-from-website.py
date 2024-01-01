'''
1. pip install pandas
'''

import pandas as pd 

# reading 1 csv file from the website
df_premier21 = pd.read_csv('https://football-data.co.uk/mmz4281/2324/E0.csv')

# showing dataframe
print(df_premier21)

# rename columns 
df_premier21.rename(columns={'FTHG':'home_goals',
                             'FTAG':'away_goals'}, inplace=True)

# show dataframe
print(df_premier21)


# if you want to save this to csv 
# df_premier21.to_csv('df_premier21.csv')
