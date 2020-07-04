#for 迴圈的基本用法
# 準備要處理的 list
name_words = ['Anna', 'April', 'Arlene', 'Basia']
# 使用 for 迴圈對 list 進行處理
for n in name_words:
    print(n)  # Anna April Arlene Basia

#for 迴圈 搭配 range 用法
for i in range(10):
    print(i)  # 0 1 2 3 4 5 6 7 8 9 

for i in range(2, 10):
    print(i)  # 2 3 4 5 6 7 8 9

test = 10
for i in range(test):
    print(i)  # 0 1 2 3 4 5 6 7 8 9 

#依照 list 的數量印出每個元素 len
fruit_list = ['apple', 'orange', 'banana', 'kiwi']
for i in range(len(fruit_list)):
    print(fruit_list[i])  # apple orange banana kiwi

#reversed method for 反向處理
number_list = [1, 2, 4, 5, 3, 100, 50 ,30 ,20]
for num in reversed(number_list):
    print(num)  # 20 30 50 100 3 5 4 2 1

#sorted method for 排序處理
fruit_list = ['apple', 'orange', 'banana', 'kiwi']
for fruit in sorted(fruit_list):
    print(fruit)  # apple banana kiwi orange

#enumerate method 自動加上索引
fruit_list = ['apple', 'orange', 'banana', 'kiwi']
for i,fruit in enumerate(fruit_list):
    print(i, ' : ', fruit)
"""
0  :  apple
1  :  orange
2  :  banana
3  :  kiwi
"""

#zip method 兩個list合併印出，簡短好閱讀
fruit_list = ['apple', 'orange', 'banana', 'kiwi']
name_list = ['mark', 'kevin', 'jarry', 'mina']

for name, fruit in zip(name_list, fruit_list):
    print(name, ' love ', fruit)
"""
mark  love  apple
kevin  love  orange
jarry  love  banana
mina  love  kiwi
"""

#for 單行 迴圈優雅的寫法
a = [i for i in range(10)]
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#透過 for 產生出1~5的整數 list
number_list = []
for i in range(1, 6):
    number_list += [i]
print(number_list)  # [1, 2, 3, 4, 5]

number_list = [i for i in range(1, 6)]
print(number_list)  # [1, 2, 3, 4, 5]

#單行 for 迴圈 儲存到新的 list
fruit_list = ['apple', 'orange', 'banana', 'kiwi']
my_fruit = []
for fruit in fruit_list:
    my_fruit.append("test %s" % fruit)
print(my_fruit)  # ['test apple', 'test orange', 'test banana', 'test kiwi']

fruit_list = ['apple', 'orange', 'banana', 'kiwi']
my_fruit = ["test %s" % fruit for fruit in fruit_list]
print(my_fruit)  # ['test apple', 'test orange', 'test banana', 'test kiwi']

#單行 for 迴圈配合 if 判斷式
number_list = [3, 4, 2, 3, 4.5, 8, 9, 8.2, 9.1, 10, 1]
get_number = [num for num in number_list if num > 8]
print(get_number)  # [9, 8.2, 9.1, 10]