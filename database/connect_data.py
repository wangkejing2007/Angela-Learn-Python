#資列印料表單一紀錄
import sqlite3
conn = sqlite3.connect('D:\Angela-Learn-Python\database\data.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from Viet_Inhabitant_Grade where 學年度=95')
row = cursor.fetchone()
if not row == None:
    print("{}\t{}\t{}".format(row[0],row[1],row[2]))
conn.close()  # 關閉資料庫連線
print()

#列印資料表所有紀錄
import sqlite3
conn = sqlite3.connect('D:\Angela-Learn-Python\database\data.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from Viet_Inhabitant_Grade')
rows = cursor.fetchall()
# print(rows)
for row in rows:
    # print("{}\t{}".format(row[0],row[1]))
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
conn.close()  # 關閉資料庫連