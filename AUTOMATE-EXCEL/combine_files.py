'''
1.pip install pandas
2.pip install DateTime
3.pip install xlrd
4.pip install plotly
5.pip install plotly-express
'''


# Imports
import pandas as pd  # Import pandas library for data manipulation
import datetime as dt  # Import datetime library for datetime operations
import calendar  # Import calendar library for calendar-related functions
import plotly  # Import Plotly for visualization
import plotly.express as px  # Import Plotly Express for simplified plotting

# Define the list of Excel file paths
files = ['AUTOMATE-EXCEL/January.xlsx', 'AUTOMATE-EXCEL/February.xlsx', 'AUTOMATE-EXCEL/March.xlsx']
# Create an empty DataFrame using pandas
combined = pd.DataFrame()

# Loop through each file in the list
for file in files:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    
    # Extract the date component and create additional columns for day, month, year, and month name
    df['Date'] = df['Date'].dt.date
    df['Day'] = pd.DatetimeIndex(df['Date']).day
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    df['Month_Name'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
    
    # Append the processed DataFrame to the combined DataFrame
    combined = combined.append(df, ignore_index=True)

# Create a bar chart using Plotly Express
fig = px.bar(combined, x='Month_Name', y='Sales', title='Sales 1Q 2020')

# Save the bar chart as an HTML file
plotly.offline.plot(fig, filename='Sales_1Q_2020.html')

# Export the combined DataFrame to an Excel file
combined.to_excel('AUTOMATE-EXCEL/Sales_1Q2020.xlsx', index=False, sheet_name='1Q 2020 Sales')


