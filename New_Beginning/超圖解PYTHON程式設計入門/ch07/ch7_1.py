# 參閱7-11頁

with open('test.txt', encoding='utf-8') as file:
    while True:
        str = file.readline()

        if (str != ''):
            print(str)
        else:
            break
