from lib.feedback import words

q_list = ['蘋果的英文？', '一打雞蛋用掉兩個，還剩下幾個？',
          '「問世間，情為何物？」的下一句？', '一天一個樣，之後又重複。（猜一天體）']
a_list = ['apple', '10', '直教生死相許', '月亮']

score = 0

for q, a in zip(q_list, a_list):
    print(q, end='  ')
    ans = input().lower().strip()

    if ans == a:
        score += 10
        msg = words(True)
    else:
        msg = words(False)

    print(msg)
    print('-' * 50)

print('總分：', score)
