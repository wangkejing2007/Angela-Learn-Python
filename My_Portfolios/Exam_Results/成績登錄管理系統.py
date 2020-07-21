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
    print("=============================================================")
    for row in cursor:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    input("按任意鍵返回主選單")
        
def input_data(): #定義新增成績紀錄  
    while True:
        item =input("請輸入新編號 (Enter==>停止輸入)：")
        if item=="": break
        elif int(item)>999 or int(item)<1: 
            print()
            print("\033[1;31m新編號 {} 不合理、請重新開始輸入紀錄！\033[0m".format(item))
            print()
            continue
        sqlstr="select * from scoretable where item='{}'" .format(item)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if not row==None:
            print("編號 {} 的紀錄已經存在!".format(item))
            continue
        # 選擇輸入日期
        date =input("請輸入登錄成績日期 (YYYY-MM-DD)：")
        if date=="": 
            print()
            print("\033[1;31m日期未輸入、請重新開始輸入紀錄！\033[0m")
            print()
            continue

        # 選擇學年度
        Schoolyear=input("請選擇學年度 --> (1)109、(2)110、(3)111：")
        if Schoolyear=="": 
            print()
            print("\033[1;31m尚未選擇學年度、請重新開始輸入紀錄！\033[0m")
            print()
            continue
        elif Schoolyear=="1":
            Schoolyear="109"
        elif Schoolyear=="2":
            Schoolyear="110"
        elif Schoolyear=="3":
            Schoolyear="111"
        else:
            print()
            print("\033[1;31m學年度代號 {} 不存在、請重新開始輸入紀錄！\033[0m".format(Schoolyear))
            print()
            continue

        # 選擇學期
        semester=input("請選擇學期代號 --> (1)上學期、(2)下學期：") 
        if semester=="1":
            semester="上學期"
        elif semester=="2":
            semester="下學期"
        else:
            print()
            print("\033[1;31m學期代號 {} 不存在、請重新開始輸入紀錄！\033[0m".format(semester))
            print()
            continue

        # 選擇考試別
        exam=input("請選擇考試別代號 --> (1)第一次月考、(2)第二次月考、(3)第三次月考：")   
        if exam=="1":
            exam="月考(1)"
        elif exam=="2":
            exam="月考(2)"
        elif exam=="3":
            exam="月考(3)"
        else:
            print()
            print("\033[1;31m考試別代號 {} 不存在、請重新開始輸入紀錄！\033[0m".format(exam))
            print()
            continue

        # 選擇考試科目
        subject=input("請選擇考試科目代號 --> (1)國語、(2)數學、(3)英文、(4)自然、(5)歷史、(6)地理：") 
        if subject=="1":
            subject="國語"
        elif subject=="2":
            subject="數學"
        elif subject=="3":
            subject="英文"
        elif subject=="4":
            subject="自然"
        elif subject=="5":
            subject="歷史"
        elif subject=="6":
            subject="地理"
        else:
            print()
            print("\033[1;31m科目代號 {} 不存在、請重新開始輸入紀錄！\033[0m".format(subject))
            print()
            continue

        # 輸入考試紀錄
        score=int(input("請輸入考試成績 (請輸入正整數)：")) 
        if score >100 or score<0:
            print()
            print("\033[1;31m輸入成績 {} 不合理、請重新開始輸入紀錄！\033[0m".format(score))
            print()
            continue
        else:
            sqlstr="insert into scoretable values('{}','{}','{}','{}','{}','{}','{}');".format(item,date,Schoolyear,semester,exam,subject,score)
            conn.execute(sqlstr)
            conn.commit()  
            print("{} 已儲存完畢".format(item))    

def edit_data(): #定義修改成績紀錄
    while True:
        item =input("請輸入要修改的紀錄編號 (Enter==>停止輸入)：")
        if item=="": break
        sqlstr="select * from scoretable where item='{}'" .format(item)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        #print(row)
        if row==None:
            print("紀錄編號 {} 不存在!".format(item))
            continue
        print("原來登記的成績為：{}".format(row[6]))
        score=input("請輸入新的成績：")
        sqlstr = "update scoretable set score='{}' where item='{}'".format(score, item)
        conn.execute(sqlstr)
        conn.commit()        
        input("成績已經更改完畢，請按任意鍵返回主選單") 
        break      

def delete_data(): #定義刪除成績紀錄
    while True:
        item =input("請輸入要刪除的紀錄編號 (Enter==>停止輸入)：")
        if item=="": break
        sqlstr="select * from scoretable where item='{}'" .format(item)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if row==None:
            print("紀錄編號 {} 不存在!".format(item))
            continue
        print("確定刪除紀錄編號 {} 的全部資料嗎？：".format(item))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            sqlstr = "delete from scoretable where item='{}'" .format(item)
            conn.execute(sqlstr)
            conn.commit()
            input("紀錄已刪除完畢，請按任意鍵返回主選單") 
            break

### 主程式從這裡開始 ###

import os,sqlite3

conn = sqlite3.connect('D:\Angela-Learn-Python\My_Portfolios\Exam_Results\Score_Register.sqlite')
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