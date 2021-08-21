# -*- coding: utf-8 -*-

import os, shutil
import pandas as pd
from openpyxl import load_workbook



    #Input_data_start = input('Введите дату начальную дату ДД.ММ.ГГГГ    ')
    #Input_data_fin = input('Введите дату конечную дату ДД.ММ.ГГГГ   ')

path = os.getcwd()
path_in = '{0}\{1}'.format(path, 'Income')
#path_out = '{0}\{1}'.format(path, 'Outcome')
report_temp='{0}\{1}\{2}'.format(path, 'Template','Template.xlsx')
file_list = os.listdir(path_in)
result=shutil.copy(report_temp,"result.xlsx")
x = 1
with pd.ExcelWriter(result,mode='a') as writer:
    for i in file_list:
    
        print(x)
        df = pd.read_excel(path_in +"\\"+ i, sheet_name="Spots" ,engine = 'openpyxl')
        newheader=df.iloc[0]
        df.columns=newheader
        df =df.iloc[1:]
        df1 = pd.DataFrame(df)
    

        
        df1.to_excel(writer, sheet_name=str(x),index=False)
        x+=1
