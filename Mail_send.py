import smtplib
from email.mime.text import MIMEText
import ssl

def send_mail(t):
    message = '温度異常です ' + t + ' ℃'
    msg = MIMEText(message, 'html')
    msg["Subject"] = 'ANESYS警報'
    msg["To"] = 'info@ownsys.jp'
    msg["From"] = 'n.miyazaki@ownsys.jp'
    #サーバ指定
    server = smtplib.SMTP('smtp6.gmoserver.jp', 587)
    server.login('info@ownsys.jp', 'ownsys3032')
    #メール送信
    server.send_message(msg)
    #閉じる
    server.quit()
    
'''
# MIMETextを作成
message = '温度異常です'
msg = MIMEText(message, 'html')
msg["Subject"] = 'ANESYS警報'
msg["To"] = 'info@ownsys.jp'
msg["From"] = 'n.miyazaki@ownsys.jp'

#サーバを指定
server = smtplib.SMTP('smtp6.gmoserver.jp', 587)
server.login('info@ownsys.jp', 'ownsys3032')
# メールを送信する
server.send_message(msg)
# 閉じる
server.quit()
'''