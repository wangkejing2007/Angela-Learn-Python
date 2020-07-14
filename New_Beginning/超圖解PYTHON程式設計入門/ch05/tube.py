# -*- coding: utf-8 -*-
import argparse
import os
from os import path
import platform
from pytube import YouTube


def pyTube_folder():
    sys = platform.system()
    home = path.expanduser('~')

    if sys == 'Windows':
        folder = path.join(home, 'Videos', 'PyTube')
    elif sys == 'Darwin':
        folder = path.join(home, 'Movies', 'PyTube')

    if not path.isdir(folder):  # 若'PyTube'資料夾不存在…
        os.mkdir(folder)           # 則新增資料夾

    return folder


def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total-remains) / total * 100
    print('下載中… {:05.2f}%'.format(percent), end='\r')

# 列舉可用的解析度


def video_res(yt):
    res_set = set()
    video_list = yt.streams.filter(type="video")
    for v in video_list:
        res_set.add(v.resolution)

    # 傳回解析度表列，例如：['720p', '480p', '360p', '240p', '144p']
    return sorted(res_set, reverse=True, key=lambda s: int(s[:-1]))


def download_video(yt, args):
    filter = yt.streams.filter

    if args.hd:
        # print ("你選擇HD畫質（720P），網址： {}".format(args.url))
        target = filter(type="video", resolution="720p").first()
    elif args.fhd:
        target = filter(type="video", resolution="1080p").first()
    elif args.sd:
        target = filter(type="video", resolution="480p").first()
    elif args.a:
        # print ("只下載聲音，網址： {}".format(args.url))
        target = filter(type="audio").first()
    else:
        # print ("網址： {}".format(args.url))
        target = filter(type="video").first()

    if target is None:
        print('沒有您指定的解析度，可用的解析度如下：')
        res_list = video_res(yt)

        for i, res in enumerate(res_list):
            print('{}) {}'.format(i+1, res))

        val = input('請選擇（預設{}）：'.format(res_list[0]))

        try:
            res = res_list[int(val)-1]
        except:  # 超出索引範圍
            res = res_list[0]

        print('您選擇的是 {} 。'.format(res))
        target = filter(type="video", resolution=res).first()

    # 開始下載
    target.download(output_path=pyTube_folder())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="指定YouTube視訊網址")
    parser.add_argument("-sd", action="store_true", help="選擇普通（480P）畫質")
    parser.add_argument("-hd", action="store_true", help="選擇HD（720P）畫質")
    parser.add_argument("-fhd", action="store_true", help="選擇Full HD（1080P）畫質")
    parser.add_argument("-a", action="store_true", help="僅下載聲音")

    args = parser.parse_args()

    try:
        yt = YouTube(args.url, on_progress_callback=onProgress)
        download_video(yt, args)
    except:
        print('下載影片時發生錯誤，請確認網路連線和YouTube網址無誤。')


if __name__ == '__main__':
    main()
