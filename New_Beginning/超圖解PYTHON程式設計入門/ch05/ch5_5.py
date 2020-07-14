# 參閱5-30頁

import os

BINPATH = r'C:\ffmpeg\bin'  # 請自行修改路徑

bps = '128k'
file = os.path.join(BINPATH, '曾經活著啊.mp4')  # 請自行修改檔名
name = os.path.join(BINPATH, '曾經活著啊')

os.system(BINPATH + r'\ffmpeg -i "{0}" -vn -ab {1} "{2}.mp3"'
          .format(file, bps, name))
