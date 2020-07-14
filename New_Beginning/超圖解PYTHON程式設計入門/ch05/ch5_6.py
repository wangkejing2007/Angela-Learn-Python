# 參閱5-31頁

import os
import argparse

FFPATH = r'C:\ffmpeg\bin\ffmpeg'  # 請自行修改路徑

parser = argparse.ArgumentParser()
parser.add_argument("src", help="來源資料夾路徑")
parser.add_argument("-b", "--bps", action="store", default='128k',
                    help="指定位元速率96, 112, 128, 160, 192, 256或320kbps")

args = parser.parse_args()
src = args.src
bps = args.bps.lower()

if bps not in ('96k', '112k', '128k', '160k', '192k', '256k', '320k'):
    bps = '128k'


def main(src):
    if os.path.isdir(src):
        for file in os.listdir(src):
            name, ext = os.path.splitext(file)
            if ext.lower() in ('.mp4', '.flac'):
                file = os.path.join(src, file)
                name = os.path.join(src, name)
                os.system(FFPATH + ' -i "{0}" -vn -ab {1} "{2}.mp3"'
                          .format(file, bps, name))


if __name__ == '__main__':
    main(src)
