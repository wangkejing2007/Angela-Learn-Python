import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

with sqlite3.connect('D:\Angela-Learn-Python\My_Portfolios\Exam_Results\Score_Register.sqlite') as con:
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='國語'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='國語'", con=con)


listx = df['item']
listy = df1['score']

plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
plt.plot(listx, listy, color ="red", label="考試成績") 
plt.legend()
plt.show()