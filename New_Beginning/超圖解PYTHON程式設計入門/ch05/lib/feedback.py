from random import choice

def words(status=True):
    right = ['好棒棒！', '讚啦!', '水喔～', '答對了！']
    wrong = ['再接再厲～', '要加油喔～', '可惜啊～']

    if status:
        msg = choice(right)
    else:
        msg = choice(wrong)

    return msg