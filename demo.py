from func import *
# ret = send_to_wecom("推送测试\r\n测试换行", "企业ID③", "应用ID①", "应用secret②");
# print( ret );
# ret = send_to_wecom('<a href="https://www.github.com/">文本中支持超链接</a>', "企业ID③", "应用ID①", "应用secret②");
# print( ret );
# ret = send_to_wecom_image("此处填写图片Base64", "企业ID③", "应用ID①", "应用secret②");
# print( ret );
# ret = send_to_wecom_markdown("**Markdown 内容**", "企业ID③", "应用ID①", "应用secret②");
# print( ret );
# 企业ID  
# 应用ID     
# 应用Secret   
compid=''
appid=''
appsecret=''

if __name__=="__main__":
    ret = send_to_wecom("server酱\r\n消息推送！", compid, appid, appsecret)
    print(ret)