import numpy as np
import pandas as pd


from matplotlib import font_manager, rc


dataset = pd.read_excel('D:/2022-2학기/캡스톤디자인/data/BUS_02_이용자유형별버스정류소이용인원현황.xlsx') 
dataset.info()

#날짜(정수형)을 문자열로 변환
dataset['base_date'] = dataset['base_date'].astype(str)  

#날짜별로 그룹핑하여 탑승객 수 집계 
temp = dataset.groupby('base_date').count() 
temp.info()

temp['탑승객수'] = temp['user_count']

 #날짜별로 그룹핑하여 탑승객 수 집계 데이터 화일로 저장
temp.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년날짜별탑승객수.xlsx')  

 #날짜별로  탑승객 수 선그래프 출력
temp.plot( y=['탑승객수'])

 #사용자 유형별로 그룹핑하여 탑승객 수 집계 
temp_user = dataset.groupby('user_type').count()

 #탑승객 수 별 내림차순 정렬
temp_user_sort = temp_user.sort_values(by='user_count', ascending=False) 

 #사용자 유형별로 그룹핑하여 탑승객 수 집계 데이터 화일로 저장
temp_user.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년사용자별탑승객수.xlsx')   
temp_user['탑승객수'] = temp_user['user_count']

#한글 출력 깨짐 방지
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

 #사용자 유형별로  탑승객 수를 선그래프 출력

temp_user.plot( y=['탑승객수'])

temp_user_sort['탑승객수'] = temp_user_sort['user_count']
temp_user_sort.plot( y=['탑승객수'])

 #정류소 별로 그룹핑하여 탑승객 수 집계 
 
temp_sn = dataset.groupby('station_name').count()

 #정류소별 탑승객 수 별 내림차순 정렬
temp_sn_sort = temp_sn.sort_values(by='user_count', ascending=False) 

 #정류소 별로  탑승객 수를 선그래프 출력
temp_sn_sort['탑승객수'] = temp_sn_sort['user_count']
temp_sn_sort.plot( y=['탑승객수'])

temp_sn.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년정류소별탑승객수.xlsx')   

#시계열 데이터 변환 및 처리 -------------------------------------

tdf = pd.read_excel('D:/2022-2학기/캡스톤디자인/data/bus2019년날짜별탑승객수.xlsx') 

tdf['base_date'] = pd.to_datetime(tdf['base_date'] )
tdf.set_index('base_date', inplace=True)
tdf.info()

tdf.head(5)

dataset.to_excel('D:/2022-2학기/캡스톤디자인/data/bus2019.xlsx')   

df = pd.read_excel('D:/2022-2학기/캡스톤디자인/data/bus2019.xlsx') 
df.info()
df.head(3)
df['일자'] = df['base_date']
df['탑승객수'] = df['user_count']

#df.set_index('base_date', inplace=True)
df.set_index('일자', inplace=True)


#df.plot( y=['탑승객수'])

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df.plot.line( y=['탑승객수'])
#df.plot.bar( y=['탑승객수'])




#CoLAB 에서 실행하기 위한 코드 -----------------------
#https://colab.research.google.com/ 로그인
import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/gdrive')

dataset = pd.read_excel('/gdrive/My Drive/data/BUS_02_이용자유형별버스정류소이용인원현황.xlsx') 
dataset.info()

from matplotlib import font_manager, rc
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib.pyplot as plt
plt.rc('font',family='NanumBarunGothic')










