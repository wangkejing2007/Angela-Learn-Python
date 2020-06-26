def menu():
    os.system("cls")
    print("成績登錄管理系統")
    print("-------------------------")
    print("1. 新增考試成績")
    print("2. 查詢考試成績")
    print("3. 修改考試成績")
    print("4. 刪除考試成績")
    print("0. 結束本程式")
    print("-------------------------")
        
def disp_data(): #顯示所有成績紀錄
    cursor = conn.execute('select * from scoretable')
    print("編號\t登錄日期\t學年度\t學期別\t考試別\t科目\t成績")
    print("===========================================================")
    for row in cursor:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    input("按任意鍵返回主選單")
        
def input_data(): #定義新增成績紀錄  
    while True:
        item =input("請輸入新編號 (Enter==>停止輸入)：")
        if item=="": break
        sqlstr="select * from scoretable where item='{}'" .format(item)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if not row==None:
            print("{} 編號已存在!".format(item))
            continue

        date =input("請輸入日期 (YYYY-MM-DD)：")
        Schoolyear=input("請輸入學年度 (109、110、111)：")
        semester=input("請輸入學期 (上學期、下學期)：") 
        exam=input("請輸入考試別 (第一次、第二次、第三次)：")     
        subject=input("請輸入科目 (國語、數學、英文、自然、歷史、地理)：") 
        score=input("請輸入考試成績 (請輸入正整數)：")       
        
        sqlstr="insert into scoretable values('{}','{}','{}','{}','{}','{}','{}');".format(item,date,Schoolyear,semester,exam,subject,score)
        conn.execute(sqlstr)
        conn.commit()  
        print("{} 已儲存完畢".format(item))    

def edit_data(): #定義修改成績紀錄
    while True:
        item =input("請輸入要修改的編號 (Enter==>停止輸入)：")
        if item=="": break
        sqlstr="select * from scoretable where item='{}'" .format(item)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        #print(row)
        if row==None:
            print("{} 帳號不存在!".format(item))
            continue
        print("原來成績為：{}".format(row[6]))
        score=input("請輸入新成績：")
        sqlstr = "update scoretable set score='{}' where item='{}'".format(score, item)
        conn.execute(sqlstr)
        conn.commit()        
        input("成績已更改完畢，請按任意鍵返回主選單") 
        break      

def delete_data(): #定義刪除成績紀錄
    while True:
        item =input("請輸入要刪除的紀錄編號 (Enter==>停止輸入)：")
        if item=="": break
        sqlstr="select * from scoretable where item='{}'" .format(item)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if row==None:
            print("{} 編號不存在!".format(item))
            continue
        print("確定刪除{}的資料!：".format(item))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            sqlstr = "delete from scoretable where item='{}'" .format(item)
            conn.execute(sqlstr)
            conn.commit()
            input("紀錄已刪除完畢，請按任意鍵返回主選單") 
            break

### 主程式從這裡開始 ###

import os,sqlite3

conn = sqlite3.connect('D:\Angela-Learn-Python\Exam_Results\Score_Register.sqlite')
while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break    

conn.close()
print("程式執行完畢！")