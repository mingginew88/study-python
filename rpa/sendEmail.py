
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 보내고자 하는 이메일 주소 리스트
names = ['xxx@gmail.com']
sender = 'xxx@naver.com'

def sendmail(sender, to, content):

    smtp_server = smtplib.SMTP("smtp.naver.com", 587)

    user = '계정명'    # 이메일 접속 계정명
    password = '비밀번호'   # 이메일 접속 비밀번호

    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo
    smtp_server.login(user, password)

    msg = MIMEMultipart('alternative')
    msg['From'] = sender                                # 보내는 사람
    msg['To'] = to                                      # 받는 사람
    msg['Subject'] = '제목'                              # 제목
    msg.attach(MIMEText(content, 'plain', 'utf-8'))     # 내용 인코딩
    smtp_server.sendmail(sender, to, msg.as_string())
    smtp_server.close()


for name in names:
    msg = (f"안녕하세요. {name}님.\n\n"
           "좋은 하루 보내세요.\n"
           "감사합니다.\n\n"
           )

    sendmail(sender, name, msg)


