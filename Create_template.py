# -*- coding: utf-8 -*-
import datetime
from datetime import date, timedelta
import re, os, fileinput, shutil,copy


    #Input_data_start = input('Введите дату начальную дату ДД.ММ.ГГГГ    ')
    #Input_data_fin = input('Введите дату конечную дату ДД.ММ.ГГГГ   ')

path = os.getcwd()
path_template = '{0}\{1}\{2}'.format(path,'Template','Template.ist')
path_result = '{0}\{1}\{2}'.format(path,'Result',"Template_midday_")
f = open(path_template, "r",encoding="utf-8")
f1 = open(path_template, "r",encoding="utf-8").readlines() #отврывает файл 
readed=f.readlines

def take_datas():
    for line in f:
        try:
            if "CTempIngrDate name=" in line:
                dats=line[29:53].split(' to ')
                print(dats)

                return dats
        except:
            print("no datas in file")

Alldata=take_datas()

Input_data_start = Alldata[0]
Input_data_fin = Alldata[1]
    
    
day, month, year  = map(int, Input_data_start.split('.'))
day2, month2, year2  = map(int, Input_data_fin.split('.'))
    
date_start = datetime.date(year, month, day)
date_fin = datetime.date(year2, month2, day2)
    
    
def Data_chek(): # проверяет порядок дат
    if date_start > date_fin:
        print('проверяет порядок дат')
        return(print("конечная дата не может быть меньше начальной"))

Data_chek()#проверка на правильность даты
    #print(str(data_list_generator()))
    
    
def mid_day():
    delta = date_fin - date_start       # считаем дельту по датам
    d=[]
    for i in range(delta.days + 1):
        day = date_fin + timedelta(days=i)
        d.append(day)
    print('считаем дельту по датам')
    return d
    
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)
    
def first_day_of_month(any_day):
    that_month = any_day.replace(day=1) 
    return that_month
    
def data_list_generator():# создает список дат для dates=
    datalist=[]
    if date_start.year==date_fin.year:
        print('создает список дат для dates')
        print(date_start.year)
        print(date_fin.year)
        for i in range(date_start.month,date_fin.month+1):
                
        
            mid_date = datetime.date(year, i, 1)
            if (date_fin.month-date_start.month) ==0:
                datalist.append(str(date_start)+"~"+str(date_fin))
                break
            
            if i == (date_start.month): 
                datalist.append(str(date_start)+"~"+str(last_day_of_month(mid_date)))
        
            
            if i == (date_fin.month): #если месяц и меньше то ставим первую и последнюю дату
                datalist.append(str(first_day_of_month(date_fin))+"~"+str(date_fin))
    
            
            if i < (date_fin.month):
                datalist.append(str(mid_date)+"~"+str(last_day_of_month(mid_date)))
        
        datalist = [re.sub('-','',i) for i in datalist]
                
        #return datalist
        
    if date_fin.year>date_start.year:
    
            max_date = datetime.date(date_start.year,12,31)
            
            for i in range(date_start.month,13):
                mid_date = datetime.date(year, i, 1)
                
                if (max_date.month-date_start.month) ==0:
                    datalist.append(str(date_start)+"~"+str(max_date))
                    print(1)
                    break
            
                if i == (date_start.month): 
                    datalist.append(str(date_start)+"~"+str(last_day_of_month(mid_date)))
                    print(2)
        
            
                if i == (max_date.month): #если месяц и меньше то ставим первую и последнюю дату
                    datalist.append(str(first_day_of_month(max_date))+"~"+str(max_date))
                    print(3)
    
            
                if i < (max_date.month+1):
                    datalist.append(str(mid_date)+"~"+str(last_day_of_month(mid_date)))
                    print(4)
            
    
            for i in range(1,date_fin.month+1):
                mid_date = datetime.date(year2, i, 1)
  
                if i == (date_fin.month):
    
                    datalist.append(str(mid_date)+"~"+str(date_fin))
                    print(5)
                        
                        
    
                if i < (date_fin.month):
                    datalist.append(str(mid_date)+"~"+str(last_day_of_month(mid_date)))   
                    print(6)
            
            datalist = [re.sub('-','',i) for i in datalist]
    return datalist   
    
            
def mid_day(): #генерирует список средних дней
    mid_day_list=[]
    start = date_start
    end = date_fin
    current = start
    mid_day_list.append(str(start))
    while current < end:
        current += timedelta(days=1)
        mid_day_list.append(str(current))
   
    mid_day_list = [re.sub('-','',i) for i in mid_day_list]
    return mid_day_list
            



def fin_file():
    for i in mid_day():
        f_name = path_result+i+".ist"
        result=open(f_name,"w",encoding='utf-8')
        file_res = copy.deepcopy(f1)
        for line in file_res:
            if line.find("PanelDate value") !=-1:
                sub = re.compile(r"PanelDate value=\D\d+")
                line = re.sub(sub, 'PanelDate value="{0}'.format(i) , line)
            if line.find("PanelType value") !=-1:
                sub = re.compile(r"PanelType value=\D\d+")
                line = re.sub(sub, 'PanelType value="{0}'.format(8) , line)
            result.writelines(line)
            result.flush()
        result.close()



print(fin_file())
    
