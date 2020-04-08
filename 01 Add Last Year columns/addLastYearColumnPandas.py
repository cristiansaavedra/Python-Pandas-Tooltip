#! python3
import os
import datetime
import pandas as pd

src_file = os.path.join(os.getcwd(),"DATA.xlsx")
df = pd.read_excel(src_file,sheet_name="DATA",index_col=None)

dfLY = df.copy()
dfLY['DATE'] = dfLY['DATE'].apply(lambda x: x.replace(year=x.year + 1))

index_PK=['DATE','ACCOUNT','SUB ACCOUNT']
df.set_index(index_PK, inplace=True)

futureYear = max(dfLY['DATE']).year
dfLY = dfLY[(dfLY['DATE'].apply(lambda x : x.year) != futureYear)].set_index(index_PK)

newCols = {'VALUE_x': 'VALUE','VALUE_y':'VALUE_LY'}
df = pd.merge(df, dfLY, how='outer', left_index=True, right_index=True).rename(columns=newCols).fillna(0).reset_index()

writer = pd.ExcelWriter("OUTPUT.xlsx")
df.to_excel(writer,sheet_name='DATA')
writer.save()