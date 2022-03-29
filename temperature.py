import sys
from func import *
import time
import os

compid=''
appid=''
appsecret=''

def run(temp,limit):
    text=f"树莓派异常！\r\n树莓派温度超过阈值（{limit}℃）\r\n当前温度:{temp}℃\t简略统计进程信息如下：\r\n"
    ret = send_to_wecom(text, compid, appid, appsecret)
    w=os.popen("w | head -n 1 | awk '{print $6,$7,$8,$9,$NF}'").read()
    top=os.popen("top -b -n 1| head -n 15 |tail -n 9|awk '{print $2,$9,$NF}'").read()
    text = w+top
    ret = send_to_wecom(text, compid, appid, appsecret)


if __name__=="__main__":
    run(sys.argv[1],sys.argv[2])