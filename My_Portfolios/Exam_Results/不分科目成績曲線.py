import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

#下面是用sqlite模組查詢資料表
with sqlite3.connect('D:\Angela-Learn-Python\My_Portfolios\Exam_Results\Score_Register.sqlite') as con:
    c = con.cursor()  
    c.execute("SELECT * FROM scoretable")
    print(c.fetchall())

with sqlite3.connect('D:\Angela-Learn-Python\My_Portfolios\Exam_Results\Score_Register.sqlite') as con:
    # 下面是用panda模組讀取資料表
    # read_sql_query和read_sql都能通过SQL语句从数据库文件中获取数据信息
    df = pd.read_sql_query("SELECT * FROM scoretable", con=con)
    # df = pd.read_sql("SELECT * FROM test_table", con=con)
    print(df.head())

listx = df['item']
listy = df['score']

plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
plt.plot(listx, listy, color ="red", label="考試成績") 
plt.legend()
plt.show()