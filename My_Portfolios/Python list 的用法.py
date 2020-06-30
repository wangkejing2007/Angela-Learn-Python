test1_list = []
test2_list = list()
print(test1_list)  # []
print(test2_list)  # []

#檢查型態使用type
print(type(test1_list))

#宣告有三個元素的list
test_list = ['a', 'b', 'c']
print(test_list) 
test_list = [123, 'Mark', 20.55, [40, 'king']]
print(type(test_list)) 

#len()，取得list的元素數量
test_list = ['a', 'b', 'c']
print(len(test_list))  

#透過布林值(boolean) in 判斷是否相同元素
test_list = [1, 2, 3, 4]
print(1 in test_list)  # True
print(5 in test_list)  # False
print('1' in test_list)  # False

#取得list中的指定元素 index
test_list = ['a', 'b', 'c']
print(test_list[1])  # b

#取得list中最後一個元素 -1
test_list = ['a', 'b', 'c']
print(test_list[-1])  # c
print(test_list[-2])  # b

#取得list超過的元素範圍，會導致錯誤：list index out of range
test_list = ['a', 'b', 'c']
#print(test_list[3])

#取得list的範圍元素 [ start : end ]
test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(test_list[3])  # d
print(test_list[0:3])  # ['a', 'b', 'c']

test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(test_list[3:])  # ['d', 'e', 'f', 'g']
print(test_list[:3])  # ['a', 'b', 'c']
print(test_list[:-1])  # ['a', 'b', 'c', 'd', 'e', 'f']

#更改 list 元素內容
test_list = ['abc', 'mark', 123]
test_list[0] = 'ccc'  
test_list[-1] = 5555
print(test_list)   # ['ccc', 'mark', 5555]

#想要一次更改多個元素
test_list = [1, 2, 3, 4, 5, 6] 
test_list[0:3] = [123, 10, 'mark'] 
print(test_list)  # [123, 10, 'mark', 4, 5, 6]

#要一次刪除多個元素
test_list = [1, 2, 3, 4, 5, 6] 
test_list[1:3] = [] 
print(test_list)  # [1, 4, 5, 6]

#append method 新增元素到list最後一位
test_list = ['a', 'b']
test_list.append('z')
print(test_list)  # ['a', 'b', 'z']

#insert method 插入元素到list指定位置
test_list = ['a', 'b']
test_list.insert(1, 'mark')
print(test_list)  # ['a', 'mark', 'b']

#extend method 兩個 list 合併為一個 list
test1_list = [1, 2, 3]
test2_list = [4, 5, 6]
test1_list.extend(test2_list)
print(test1_list)  # [1, 2, 3, 4, 5, 6]

#del method 刪除list指定位置
test_list = ['a', 'b', 'c', 'd']
del test_list[1]
print(test_list)  # ['a', 'c', 'd']

#remove method 刪除 list指定元素
test_list = ['a', 'b', 'c', 'd']
test_list.remove('b')
print(test_list)  # ['a', 'c', 'd']

#pop method 移除list中最後一個元素
test_list = ['a', 'b', 'c', 'd']
test_list.pop()  # 'd'
print(test_list)  # ['a', 'b', 'c']

#count method 計算list指定元素出現次數
test_list = ['king', 'kevin', 'mark', 'jarry', 'mark']
print(test_list.count('mark'))  # 2

#sorted method 排序你的list
test_list = [24, 45, 30, 12, 31, 222, 1, 3]
print(sorted(test_list))  # [1, 3, 12, 24, 30, 31, 45, 222]

#sorted method 也可以反排序你的list
test_list = [24, 45, 30, 12, 31, 222, 1, 3]
print(sorted(test_list, reverse = True))  # [222, 45, 31, 30, 24, 12, 3, 1]

#split method 將 Str to List (字串轉列表)
test_word = 'how are you'
words = test_word.split()
print(words)  # ['how', 'are', 'you']

number_word = '1,2,3,4,5,6,7,8,9'
words = number_word.split(',')
print(words)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

name_word = 'Aaron.Abbott.Alvis.Bob'
words = name_word.split('.')
print(words)  # ['Aaron', 'Abbott', 'Alvis', 'Bob']

# https://markteaching.com/python-list/?fbclid=IwAR1fR1lw5tPOfkAL1dlCxHApHg8h6857xZsoG-fsUh1RsAjLOPvqvXH6ezY