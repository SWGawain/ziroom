# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 发送邮件的邮箱
from_addr = ""
# 发送邮件的密码
password = ""
# 发送给谁 ，用','分割
to_addr = [""]
smtp_server = "smtp.qq.com"
# 房源名称
room_name = "茉莉园12号楼1101"
# ziroom页面上房源编号
room = 116152

msg = MIMEText(room_name+"可以预定了", 'plain', 'utf-8')
msg['From'] = from_addr
msg['Subject'] = Header('ziroom房源状态变更……', 'utf-8').encode()
msg['To'] = ','.join(to_addr)

def sendNotice():
    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print("邮件发送完成")