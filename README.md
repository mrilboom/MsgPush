# 树莓派温度检测与温度异常推送

树莓派的温度信息记录在 `/sys/class/thermal/thermal_zone0/temp` 这个文件中，该数据除以1000就是正常的摄氏度温度，设定每隔一段时间对温度进行采集判断，温度如果超过设定好的阈值，就会触发推送，推送当前树莓派温度、系统近期负载以及进程列表等信息。

## 推送部分采用的是[server酱](https://sct.ftqq.com/forward)

该方法完全免费，同时配置较为方便，而且一次配置之后通过 api 调用即可，无需再上到后台进行配置。


## 配置过程
### 配置api
依照 server 酱的教程，获取
* 企业ID  
* 应用ID     
* 应用Secret  
填入 temperature.py 中
### 配置 service
配置好 service 中的 WorkingDirectory 工作目录，之后将 service 文件移到 /etc/systemd/system/ 文件夹下，启动服务即可
```bash
mv WatchTemp.service  /etc/systemd/system/
sudo systemctl enable WatchTemp #开机自启动
sudo systemctl start WatchTemp  #启动服务
```