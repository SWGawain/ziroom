# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import smtplib

from_addr = "395772584@qq.com"
password = "Wain920213"
to_addr = ["395772584@qq.com","wangjiawei@facebank.cn"]
smtp_server = "smtp.qq.com"
room = 116152

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = from_addr
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
msg['To'] = ','.join(to_addr)

def sendNotice():
    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print("邮件发送完成")