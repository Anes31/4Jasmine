import pandas as pd

#write the file name (add the path if the file isn't in the same folder as this script)
fileName = 'Copy of 2018 ASP RankingF (00000002)'

df = pd.read_excel( fileName + '.xlsx', sheet_name='Labor', usecols='J,AC')

size = df.groupby(df.columns.tolist()).size()
temp = size.to_frame(name = 'size').reset_index()

temp = temp[temp['size']>1]
res = temp.groupby('Customer Name').size()
df_output = res.to_frame(name = '>1').reset_index()

df_output.to_csv('Result.csv', index=False)