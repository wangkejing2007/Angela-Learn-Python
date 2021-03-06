import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

sequence_length = 10  #特徵資料個數
split = 0.95  #訓練資料比率

pd.options.mode.chained_assignment = None  #取消顯示pandas資料重設警告
filename = 'twstock_all.csv'
df = pd.read_csv(filename, encoding='big5')  #以pandas讀取檔案
dfprice=pd.DataFrame(df['收盤價'])
    
data_all = np.array(dfprice).astype(float)  #轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  #將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length):
    data.append(data_all[i: i + sequence_length + 1])  #每筆data資料有11欄
reshaped_data = np.array(data).astype('float64')
x = reshaped_data[:, :-1]  #第1至第10個欄位為特徵
y = reshaped_data[:, -1]   #第11個欄位為Label
split_boundary = int(reshaped_data.shape[0] * split)  #分離資料
train_x = x[: split_boundary]  #訓練特徵資料
test_x = x[split_boundary:]  #test特徵資料
train_y = y[: split_boundary]  #訓練label資料
test_y = y[split_boundary:]   #test的label資料

model = Sequential()     
model.add(LSTM(input_shape=(sequence_length,1),units=256,unroll=False))  #LSTM層
model.add(Dense(units=1)) #輸出層：1個神經元
model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])
model.fit(train_x, train_y, batch_size=100, epochs=300, validation_split=0.1,verbose=2)

model.save('Stock_rnn_model.h5')  #儲存模型
print("\nStock_rnn_model.h5 模型儲存完畢!")

