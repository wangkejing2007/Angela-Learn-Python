from apscheduler.schedulers.background import BackgroundScheduler
import os
import time

def bid():
    cmd = "python ./mybid_sheet.py"
    # cmd = "python ./hello.py"
    os.system(cmd)

if __name__ == "__main__":
    # 新增工作排程
    sch = BackgroundScheduler()
    sch.add_job(bid,'interval', minutes=10)
    sch.start()
    print('工作排程開始，按Ctrl+C結束。')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sch.shutdown()
        print('工作排程結束～')
