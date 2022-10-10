# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:49:59 2022

@author: User
"""

import numpy as np
import pandas as pd


from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


a = np.arange(1,6)
b = pd.date_range("2019-09-01", periods=5, freq="D")
s = pd.Series(a,index=b)
s
dataset = pd.read_excel('D:/2022-2학기/캡스톤디자인/data/BUS_02_이용자유형별버스정류소이용인원현황.xlsx') 
dataset.info()
dataset['base_date'][0]

dataset['base_date'] = dataset['base_date'].astype(str)

temp = dataset.groupby('base_date').count()
temp.info()

temp['탑승객수'] = temp['user_count']
temp.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년날짜별탑승객수.xlsx')   
temp.plot( y=['탑승객수'])

temp_user = dataset.groupby('user_type').count()
temp_user_sort = temp_user.sort_values(by='user_count', ascending=False)
temp_user.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년사용자별탑승객수.xlsx')   

temp_sn = dataset.groupby('station_name').count()
temp_sn.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년정류소별탑승객수.xlsx')   


dataset['base_date'] = pd.to_datetime(dataset['base_date'] )
dataset.set_index('base_date', inplace=True)
dataset.info()

dataset.head(5)

dataset.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019.xlsx')   

df = pd.read_excel('D:/2022-2학기/캡스톤디자인/data/bus2019.xlsx') 
df.info()
df.head(3)
df['일자'] = df['base_date']
df['탑승객수'] = df['user_count']

#df.set_index('base_date', inplace=True)
df.set_index('일자', inplace=True)


#df.plot( y=['탑승객수'])

df.plot.line( y=['탑승객수'])
#df.plot.bar( y=['탑승객수'])
