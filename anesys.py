import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
import matplotlib


st.title('ANESYS')



#csv
year = dt.datetime.today().strftime('%Y')
month = dt.datetime.today().strftime('%m')
day = dt.datetime.today().strftime('%d')


#df = pd.read_csv('ANESYS/Data/' + year + '/' + month + '_' + day + '.csv', names = ['datetime', '温度', '湿度'])
df = pd.read_csv('Data/' + year + '/' + month + '_' + day + '.csv', names = ['datetime', '温度', '湿度'])
name = 'ハウス1'

df2 = df.tail(1)#末尾1
df2 = df2.set_index('datetime')
df2 = df2.reset_index(drop=True)
df2 = df2.rename({0:name})
df2.loc[name, '温度'] = str(df2.iat[0, 0]) + ' ℃'
df2.loc[name, '湿度'] = str(int(df2.iat[0, 1])) + ' ％'
st.table(df2)


#####Graph#######
selected_day = dt.datetime.today()

selected_day = st.date_input('', value = selected_day,max_value=dt.datetime.today())

year = selected_day.strftime('%Y')
month = selected_day.strftime('%m')
day = selected_day.strftime('%d')


try:
    #g_df = pd.read_csv('ANESYS/Data/' + year + '/' + month + '_' + day + '.csv', names = ['datetime', '温度', '湿度', 'CO2', '日射量'])
    g_df = pd.read_csv('Data/' + year + '/' + month + '_' + day + '.csv', names = ['datetime', '温度', '湿度', 'CO2', '日射量'])
    g_df['datetime'] = pd.to_datetime(g_df['datetime'])
    
    #Graph_Font
    plt.rcParams['font.family'] = 'VL Gothic'
    
    #fig = plt.figure()
    fig, ax = plt.subplots()
    ax.plot(g_df['datetime'], g_df['温度'], color='r')#データ
    ax.set_ylabel('温度', color='r',  labelpad=-10)#ラベル色・位置
    ax.spines['left'].set_color('r')#軸縦の色
    ax.tick_params(axis = 'y', colors ='r')#軸目盛の色
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))#X軸の間隔
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H"))#X軸のフォーマット
    ax.set_xlim(selected_day, selected_day + dt.timedelta(days=1))#X軸の範囲
    ax.set_ylim(0,50)#X軸の範囲
    ax.spines['top'].set_alpha(0.1)#上枠

    ax.grid(color='gray', alpha = 0.5, linestyle='dotted')#目盛線

    ax2 = ax.twinx()
    ax2.plot(g_df['datetime'], g_df['湿度'], color='b')
    ax2.set_ylabel('湿度', color='b', labelpad=-15)#label_color
    ax2.tick_params(axis = 'y', colors ='b')#maingrid_colr
    ax2.xaxis.set_major_locator(mdates.HourLocator(interval=3))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H"))#X軸のフォーマット
    #ax2.set_xlim(dt.datetime(2022,3,7),dt.datetime(2022,3,8))
    ax2.spines["right"].set_position(("axes", 1))
    ax2.set_ylim(0,100)
    ax2.spines['top'].set_alpha(0.1)#upper_frame

    ax2.spines['left'].set_color('r')
    ax2.spines['right'].set_color('b')

    st.pyplot(plt)

except:
    st.write('データがありません')
    

