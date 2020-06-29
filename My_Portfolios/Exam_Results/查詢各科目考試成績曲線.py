#定義選單功能
def menu():
    os.system("cls")
    print("成績登錄管理系統")
    print("-------------------------")
    print("1. 國語科成績")
    print("2. 數學科成績")
    print("3. 自然科成績")
    print("4. 歷史科成績")
    print("5. 地理科成績")
    print("0. 結束本程式")
    print("-------------------------")

#定義國語科曲線圖
def Chinese_Score():
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='國語'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='國語'", con=con)
    listx = df['item']
    listy = df1['score']
    plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
    plt.title("國語科考試紀錄曲線表")
    plt.xlabel("紀錄編號")
    plt.ylabel("考試成績")
    #plt.xlim(109,111)
    #plt.ylim(0,100)
    #plt.grid(True)
    plt.plot(listx, listy, color ="blue", label="成績曲線") 
    plt.legend()
    plt.show()

#定義數學科曲線圖
def Math_Score():
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='數學'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='數學'", con=con)
    listx = df['item']
    listy = df1['score']
    plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
    plt.title("數學科考試紀錄曲線表")
    plt.xlabel("紀錄編號")
    plt.ylabel("考試成績")
    plt.grid(True)
    plt.plot(listx, listy, color ="blue", label="成績曲線") 
    plt.legend()
    plt.show()

#定義英文科曲線圖
def English_Score():
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='英文'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='英文'", con=con)
    listx = df['item']
    listy = df1['score']
    plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
    plt.title("英文科考試紀錄曲線表")
    plt.xlabel("紀錄編號")
    plt.ylabel("考試成績")
    plt.grid(True)
    plt.plot(listx, listy, color ="blue", label="成績曲線") 
    plt.legend()
    plt.show()

#定義自然科曲線圖
def Natural_Score():
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='自然'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='自然'", con=con)
    listx = df['item']
    listy = df1['score']
    plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
    plt.title("自然科考試紀錄曲線表")
    plt.xlabel("紀錄編號")
    plt.ylabel("考試成績")
    plt.grid(True)
    plt.plot(listx, listy, color ="blue", label="成績曲線") 
    plt.legend()
    plt.show()

#定義歷史科曲線圖
def History_Score():
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='歷史'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='歷史'", con=con)
    listx = df['item']
    listy = df1['score']
    plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
    plt.title("歷史科考試紀錄曲線表")
    plt.xlabel("紀錄編號")
    plt.ylabel("考試成績")
    plt.grid(True)
    plt.plot(listx, listy, color ="blue", label="成績曲線") 
    plt.legend()
    plt.show()

#定義地理科曲線圖
def Geography_Score():
    df = pd.read_sql_query("SELECT * FROM scoretable where subject='地理'", con=con)
    df1 = pd.read_sql_query("SELECT * FROM scoretable where subject='地理'", con=con)
    listx = df['item']
    listy = df1['score']
    plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
    plt.title("地理科考試紀錄曲線表")
    plt.xlabel("紀錄編號")
    plt.ylabel("考試成績")
    plt.grid(True)
    plt.plot(listx, listy, color ="blue", label="成績曲線") 
    plt.legend()
    plt.show()

### 主程式從這裡開始 ###
import os,sqlite3
import matplotlib.pyplot as plt
import pandas as pd

with sqlite3.connect('D:\Angela-Learn-Python\My_Portfolios\Exam_Results\Score_Register.sqlite') as con:
    while True:
        menu()
        choice = int(input("請輸入您的選擇："))
        print()
        if choice==1:
            Chinese_Score()
        elif choice==2:
            Math_Score()
        elif choice==3:
            English_Score()
        elif choice==4:
            Natural_Score()
        elif choice==5:
            History_Score()
        elif choice==6:
            Geography_Score()
        else:
            break    

con.close()
print("程式執行完畢！")