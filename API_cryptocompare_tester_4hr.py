#!/usr/bin/env python
# coding: utf-8

# # Crytocomare API
# 

# ## Reference:  
#   
# **[比特幣程式交易] 如何透過API獲取比特幣歷史報價數據?**  
# **YouTube**:https://www.youtube.com/watch?v=no5dBXTppkg&ab_channel=%E5%A4%A7%E6%95%B8%E8%BB%9F%E9%AB%94%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8
# **Github**:https://github.com/ywchiu/largitdata/blob/master/code/Course_138.ipynb  
# 
# **Crytocomare API**:https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistohour

# ## API 指令
# fsym= (後面放從什麼幣值轉換）  
# tsym= (後面放轉換成什麼幣值）  
# 這裡是從比特幣轉換成美金  
# limit= (後面放限制回傳資料筆數）  
# aggregate= (後面放間隔時間）  
# 這裡是每**間隔4小時**一筆資料，每天6筆資料  
# 
#   
# 結果**Response [200]** 代表API請求成功

# In[3]:


import requests
res = requests.get("https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=168&aggregate=4")
res


# In[ ]:


res.json()


# In[ ]:


res.json()["Data"]["Data"]


# ## 檢查資料
# 將得到的資料利用pandas轉為DataFrame資料型態，並繪製成表格檢查資料

# In[5]:


import pandas
df = pandas.DataFrame(res.json()["Data"]["Data"])
df.head()


# 將以unix時間為單位的日期轉為正常日期

# In[6]:


df['time'] = pandas.to_datetime(df['time'], unit = 's')
df.head()


# ## 繪製K線圖 (candlestick)  
#   
# doc:https://plotly.com/python/candlestick-charts/  
# Bitfinex:https://trading.bitfinex.com/t/BTC:USD?type=exchange

# In[7]:


import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x=df['time'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.show()


# In[ ]:




