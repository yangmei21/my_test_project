import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import formataddr


def send_email():
    user = '2168517841@qq.com'
    pwd = 'abdabccfmblreajg'
    to = '1154372391@qq.com'

    # 创建一个可以同时添加正文和附件的msg
    msg = MIMEMultipart()

    # 设置HTML格式的邮件正文
    mail_msg = '''
    <p>这里是一个登录测试报告邮件，请查收！附件内(*^▽^*)
    <p><a href="https://www.baidu.com">这里是链接</a>
    '''
    msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))  # 添加正文

    # 添加附件
    file_path = './reports/userlogin_report.html'
    with open(file_path, 'r', encoding='gbk') as file:
        file_content = file.read()

    att1 = MIMEText(file_content, 'html', 'utf-8')
    att1["Content-Disposition"] = 'attachment;filename="yx_login.html"'
    msg.attach(att1)

    # 设置邮件主题
    subject = '测试报告邮件（yx登录测试报告）'
    msg['Subject'] = Header(subject, 'utf-8').encode()

    # 设置发件人和收件人
    msg['From'] = formataddr(('Sender', user))
    msg['To'] = to

    try:
        # 连接 SMTP 服务器
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(user, pwd)  # 登录QQ邮箱
        s.sendmail(user, to, msg.as_string())  # 发送邮件
        s.quit()  # 退出QQ邮箱服务
        print('Success')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    send_email()
