def menu():
    os.system("cls")
    print("全國中小學就學人數查詢系統")
    print("-----------------------------------------")
    print("1. 全國中小學就讀總人數(依性別)")
    print("2. [新住民子女]中小學就讀人數(依性別)")
    print("3. [越南新住民子女]中小學就讀人數(依性別)")
    print("4. [越南新住民子女]中小學就讀人數(依年級)")
    print("0. 結束本查詢程式")
    print("-----------------------------------------")
        

def chose_1():
    #cursor = conn.execute('select * from All_Elem_Enrol')
    print("全國中小學就讀總人數(依性別)")
    cur = conn.cursor()
    cur.execute("select * from All_Elem_Enrol") 
    table = from_db_cursor(cur)
    table.align="r"
    print(table)
    input("按任意鍵返回主選單")  
    
     
def chose_2():
    #cursor = conn.execute('select * from New_Inhabitant')
    print("[新住民子女]中小學就讀人數(依性別)")
    cur = conn.cursor()
    cur.execute("select * from New_Inhabitant") 
    table = from_db_cursor(cur)
    table.align="r"
    print(table)
    input("按任意鍵返回主選單")  

def chose_3():
    #cursor = conn.execute('select * from Viet_Inhabitant_Gender')
    print("[越南新住民子女]中小學就讀人數(依性別)")
    cur = conn.cursor()
    cur.execute("select * from Viet_Inhabitant_Gender") 
    table = from_db_cursor(cur)
    table.align="r"
    print(table)
    input("按任意鍵返回主選單")  
     
def chose_4():
    #cursor = conn.execute('select * from Viet_Inhabitant_Grade')
    print("[越南新住民子女]中小學就讀人數(依年級)")
    cur = conn.cursor()
    cur.execute("select * from Viet_Inhabitant_Grade") 
    table = from_db_cursor(cur)
    table.align="r"
    print(table)
    input("按任意鍵返回主選單")  
     
     
### 主程式從這裡開始 ###

import os,sqlite3
#import sys
from prettytable import PrettyTable
from prettytable import from_db_cursor 

conn = sqlite3.connect('D:/Angela-Learn-Python/My_Portfolios/My_Essay/New_Immigrants/enrolment.sqlite')
while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice==1:
        chose_1()
    elif choice==2:
        chose_2()
    elif choice==3:
        chose_3()
    elif choice==4:
        chose_4()
    elif choice==0:
        break
    else:
        input("輸入錯誤，請按任意鍵返回主選單！")   
          
conn.close()
print("本查詢程式執行完畢！")
print()