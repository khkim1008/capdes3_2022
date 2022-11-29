# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 05:59:11 2022

@author: By 
"""

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname = font_path).get_name()
matplotlib.rc('font', family=font_name)

#!pip install folium
import folium


def run():
    fn1 = 'D:/2022-2학기/캡스톤디자인/new/사용자유형별_정류소_이용현황.csv'
    fn2 = 'D:/2022-2학기/캡스톤디자인/new/버스정류소_위치.xlsx'
    f1 = pd.read_csv(fn1, encoding='cp949')
    #f1 = pd.read_excel(fn1) 
    f1.info()
    f2 = pd.read_excel(fn2) 
    f2.info()
    f2.rename(columns = {'정류소명':'station_name'}, inplace=True)
    
    
    정류소별_탑승객수 = f1.groupby(['station_name'])['user_count'].sum()
    정류소별_탑승객수.info()
    정류소별_탑승객수 = 정류소별_탑승객수.reset_index()
    
    정류소별_유형별_탑승객수 = f1.groupby(['station_name', 'user_type'])['user_count'].sum()
    정류소별_유형별_탑승객수.info()
    정류소별_유형별_탑승객수 = 정류소별_유형별_탑승객수.reset_index() # 기본키(인덱스)로 묶였던 컬럼들을 개별로 풀어줌 (index rebuild)

    temp = 정류소별_유형별_탑승객수.user_type.unique()

    for 사용자유형 in temp:
        print(사용자유형)
        tn  = 정류소별_유형별_탑승객수.loc[정류소별_유형별_탑승객수['user_type'] == 사용자유형,:]
        if 사용자유형 == '경로':
            정류소별_경로_탑승객수 = tn
        elif 사용자유형 == '일반':     
            정류소별_일반_탑승객수 = tn
        elif 사용자유형 == '장애 동반':         
            정류소별_장애동반_탑승객수 = tn
        elif 사용자유형 == '장애 일반':
            정류소별_장애일반_탑승객수 = tn          
        elif 사용자유형 == '청소년':     
            정류소별_청소년_탑승객수 = tn        
        elif 사용자유형 == '어린이':     
            정류소별_어린이_탑승객수 = tn
        elif 사용자유형 == '유공 일반':     
            정류소별_유공일반_탑승객수 = tn
        elif 사용자유형 == '유공 동반':
            정류소별_유공동반_탑승객수 = tn   
        else:
            정류소별_유공동반_탑승객수 = tn   
         
    정류소별_장애_탑승객수 = pd.concat([정류소별_장애동반_탑승객수, 정류소별_장애일반_탑승객수]) 
    정류소별_유공_탑승객수 = pd.concat([정류소별_유공동반_탑승객수, 정류소별_유공일반_탑승객수]) 
    정류소별_일반_탑승객수  =  정류소별_유형별_탑승객수.loc[정류소별_유형별_탑승객수['user_type'] == '일반',:]
    정류소별_유형별_탑승객수_정렬 = 정류소별_유형별_탑승객수.sort_values(by = 'user_count', ascending=False)
    전체탑승객수_2019 = 정류소별_유형별_탑승객수['user_count'].sum()
    
    # -------- 사용자 유형: 전체 --------------
    
    정류소별_탑승객수_top10 = 정류소별_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기(정류소별_탑승객수_top10, '전체')    
    정류소별_탑승객수_top10_위치 = pd.merge(정류소별_탑승객수_top10, f2, how='inner')
    지도시각화(정류소별_탑승객수_top10_위치, '전체')
    

    # -------- 사용자 유형: 일반 --------------
    일반_탑승객수_2019 = 정류소별_일반_탑승객수['user_count'].sum()
    일반비율 = 일반_탑승객수_2019/전체탑승객수_2019      # 약 64%
    정류소별_일반_탑승객수_top10 = 정류소별_일반_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기(정류소별_일반_탑승객수_top10, '일반')
    정류소별_일반_탑승객수_top10_위치 = pd.merge(정류소별_일반_탑승객수_top10, f2, how='inner')
    지도시각화(정류소별_일반_탑승객수_top10_위치, '일반')
    
    
    
    
    
    # -------- 사용자 유형: 경로 --------------
    경로_탑승객수_2019 = 정류소별_경로_탑승객수['user_count'].sum()
    경로비율 = 경로_탑승객수_2019/전체탑승객수_2019  #약 14%
    정류소별_경로_탑승객수_top10 = 정류소별_경로_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기( 정류소별_경로_탑승객수_top10, '경로')
    정류소별_경로_탑승객수_top10_위치 = pd.merge(정류소별_경로_탑승객수_top10, f2, how='inner')
    지도시각화(정류소별_경로_탑승객수_top10_위치, '경로')
    
    # -------- 사용자 유형: 어린이 --------------
    어린이_탑승객수_2019 = 정류소별_어린이_탑승객수['user_count'].sum()
    어린이비율 = 어린이_탑승객수_2019/전체탑승객수_2019  # 약 2%
    정류소별_어린이_탑승객수_top10 = 정류소별_어린이_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기(정류소별_어린이_탑승객수_top10, '어린이')
    
    # -------- 사용자 유형: 청소년 --------------
    청소년_탑승객수_2019 = 정류소별_청소년_탑승객수['user_count'].sum()
    청소년비율 = 청소년_탑승객수_2019/전체탑승객수_2019  # 약 13%
    정류소별_청소년_탑승객수_top10 = 정류소별_청소년_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기(정류소별_청소년_탑승객수_top10, '청소년')
    
    # -------- 사용자 유형: 유공 --------------
    유공_탑승객수_2019 = 정류소별_유공_탑승객수['user_count'].sum()
    유공비율 = 유공_탑승객수_2019/전체탑승객수_2019   #약 0.5%
    정류소별_유공_탑승객수_top10 = 정류소별_유공_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기(정류소별_유공_탑승객수_top10, '유공')
    
    # -------- 사용자 유형: 장애 --------------
    장애_탑승객수_2019 = 정류소별_장애_탑승객수['user_count'].sum()
    장애비율 = 장애_탑승객수_2019/전체탑승객수_2019  # 약 5% 
    정류소별_장애_탑승객수_top10 = 정류소별_장애_탑승객수.sort_values(by = 'user_count', ascending=False).head(10)
    Top10정류소_막대그래프_그리기(정류소별_장애_탑승객수_top10, '장애')
    
    TR = 일반비율 + 경로비율 + 어린이비율 + 청소년비율 + 유공비율 + 장애비율
    사용자유형별_버스정류소_사용비율_파이시각화(일반비율, 경로비율, 어린이비율, 청소년비율, 유공비율, 장애비율)
    
    
    #------------- 막대그래프 그리기 -----------------
    

def Top10정류소_막대그래프_그리기(df, title):
    dic  = dict() 
    for index, row in df.iterrows():
        print(row.station_name)
        dic[row.station_name] = row.user_count
    
    plt.figure(figsize=(10,5))
    plt.xlabel('정류소')
    plt.ylabel('탑승객수')
    plt.grid(True)
    plt.title(title+ '_탑승객 이용 버스정류장 Top10 순위')

    sorted_Keys = sorted(dic, key=dic.get, reverse=True)
    sorted_Values = sorted(dic.values(), reverse=True)
    
    
    plt.bar(range(len(dic)), sorted_Values, align='center')
    plt.xticks(range(len(dic)), list(sorted_Keys), rotation='90')
    dirname = 'D:/2022-2학기/캡스톤디자인/new/result/'
    graph_name = dirname + title + '_막대그래프.png'
    plt.savefig(graph_name, bbox_inches = 'tight')
    plt.show()
    
def  사용자유형별_버스정류소_사용비율_파이시각화(일반비율, 경로비율, 어린이비율, 청소년비율, 유공비율, 장애비율):
    ratio = [일반비율, 경로비율, 어린이비율, 청소년비율, 유공비율, 장애비율]
    labels = ['일반인', '경로인', '어린이', '청소년', '국가유공자', '장애인']

    plt.title('사용자유형_버스정류소_이용비율')
    plt.pie(ratio, labels=labels, autopct='%.1f%%')
    dirname = 'D:/2022-2학기/캡스톤디자인/new/result/'
    graph_name = dirname + '사용자유형_버스이용비윻_파이챠트.png'
    plt.savefig(graph_name, bbox_inches = 'tight')
    plt.show()   

def 지도시각화(정류소별_탑승객수_top10_위치, title):
    map_osm = folium.Map(location=[33.3866, 126.5304], zoom_start=11) #제주 한라산 주변의 위도 및 경도 값 
    
    for item in 정류소별_탑승객수_top10_위치.index:
        lat = 정류소별_탑승객수_top10_위치.loc[item, '위도']
        long = 정류소별_탑승객수_top10_위치.loc[item, '경도']
        folium.CircleMarker([lat, long],
                            radius = 정류소별_탑승객수_top10_위치.loc[item, 'user_count']/50000,
                            popup = 정류소별_탑승객수_top10_위치.loc[item, 'station_name'] ,
                            color = 'blue',
                            fill = True).add_to(map_osm)
    dirname = 'D:/2022-2학기/캡스톤디자인/new/result/'
    
    map_name = dirname + title +'_사용자_Top10_정류소_지도표시.html'
    map_osm.save(map_name)
    

if __name__ == "__main__":
    print("버스정류소 이용자 분석")
    run()  























