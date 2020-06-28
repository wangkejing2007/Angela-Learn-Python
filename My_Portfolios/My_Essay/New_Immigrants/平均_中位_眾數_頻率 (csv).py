import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 讀入score.csv
dat = pd.read_csv('D:\\Angela-Learn-Python\\My_Portfolios\\My_Essay\\New_Immigrants\\All_ElemSecon.csv', encoding='UTF-8')
print(dat.head)


# 平均數、中位數
print('平均數', round(np.mean(dat['國中小總計']),2)) #round()取小數點位數
print('中位數', np.median(dat['國中小總計']))

# 眾數
bincnt = np.bincount(dat['國中小總計'])  # 計算同樣的值的個數
mode = np.argmax(bincnt)  # 取得bincnt中最大的值
print('眾數', mode)

# 計算各組別頻率
hist = [0]*7 # 頻率（分組數設為7組，初始化為0）

for dat in dat['國中小總計']:
    if dat < 1600000:   hist[0] += 1
    elif dat < 1800000:  hist[1] += 1
    elif dat < 2000000:  hist[2] += 1
    elif dat < 2200000:  hist[3] += 1
    elif dat < 2400000:  hist[4] += 1
    elif dat < 2600000:  hist[5] += 1
    elif dat < 2800000:  hist[6] += 1
print('頻率:', hist)

# 頻率分布圖
x = list(range(1,8))  # x軸的值
labels = ['1.6m','1.8m','2.0m','2.2m','2.4m','2.6m','2.8m']  # x軸的刻度標籤
plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
plt.bar(x, hist, tick_label=labels, width=1)# 描繪長條圖
plt.show()