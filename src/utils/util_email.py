# -*- coding: utf-8 -*-
# script for python3.2
import os, sys
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.encoders import encode_base64



class Mail():
    # 初始化
    def __init__(self, user, pwd, host):
        self.mail_user = user
        self.mail_pwd = pwd
        self.mail_server = smtplib.SMTP_SSL()
        self.mail_server.connect(host)
        self.mail_server.ehlo()
        self.mail_server.login(self.mail_user, self.mail_pwd)

    def __del__(self):
        self.mail_server.close()

    # 发送邮件
    def send_mail(self, recipient, subject, text, file_path):
        msg = MIMEMultipart()
        msg["From"] = self.mail_user
        msg["Subject"] = subject
        msg["To"] = ",".join(recipient)
        msg.attach(MIMEText(text))
        msg.attach(self.get_attachment(file_path))
        self.mail_server.sendmail(self.mail_user, recipient, msg.as_string())
        print("邮件发送成功")

    # 添加邮件附件
    def get_attachment(self, file_path):
        file_name = file_path.split("\\")[-1]
        attachment = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        attachment["Content-Type"] = 'application/octet-stream'
        attachment["Content-Disposition"] = 'attachment; filename=' + file_name
        return attachment


if __name__ == '__main__':
    title = "自动化测试报告测试"
    content = "web端自动化测试报告"
    path = "C:\\Users\\SNake\\PycharmProjects\\scmcc_web\\report\\2018-04-09\\TEST_CASE_2018_04_09 11_20_09.html"
    mail = Mail(MAIL_QQ_USER, MAIL_QQ_PWD, MAIL_QQ_HOST)
    mail.send_mail(title, content, path)

