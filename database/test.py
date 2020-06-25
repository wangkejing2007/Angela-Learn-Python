import sqlite3
conn = sqlite3.connect('data.sqlite') # 建立資料庫連線

cursor = conn.execute('select * from All_ElemSecon where 學年度=96')

row = cursor.fetchone()

if not row == None:
    print("{}\t{}\t{}".format(row[1],row[2],row[3]))

conn.close()  # 關閉資料庫連