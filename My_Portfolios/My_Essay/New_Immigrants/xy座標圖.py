import matplotlib.pyplot as plt
import pandas as pd

# 讀入score.csv
dat = pd.read_csv('D:\\Angela-Learn-Python\\My_Portfolios\\My_Essay\\New_Immigrants\\All_ElemSecon.csv', encoding='UTF-8')

#第一條線
listx = dat['學年度']
listy = dat['國中合計']/10000 #單位換算成萬
#第二條線
listx1 = dat['學年度']
listy1 = dat['國小合計']/10000 #單位換算成萬

plt.rcParams['font.sans-serif']=['SimHei'] #要自己設定字體，要不然中文會變亂碼
plt.title("全國中小學就讀總人數變化曲線表")

plt.xlabel("(學年度)")
plt.ylabel("學生人數(單位:萬)")

plt.plot(listx, listy, color ="red", label="國中合計") #國中合計
plt.plot(listx1, listy1, color ="green", label="國小合計") #國小合計

plt.legend()
plt.show()