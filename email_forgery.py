# coding:utf-8
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'zhangsan@th.com'  # 发件人邮箱账号
my_pass = '123123123'  # 发件人邮箱密码(当时申请smtp给的口令)

pwd = '/Users/shukasakai/Desktop/test.txt'
victim_list = []
with open(pwd, 'r') as temporary_file:
    for i in temporary_file:
        i = i.strip()
        # i = i.lower()
        victim_list.append(i)

i = 1
# for i in victim_list:
#     victim_name.append(i.split(':')[0])
#     victim_email.append(i.split(':')[1])

def mail(a):
    global i
    for zx in range(len(victim_list)):
        email = victim_list[zx]
        ret = True
        text = '''
                邮件内容
        '''
        try:
            msg = MIMEMultipart('related')
            msg.attach(MIMEText('{}'.format(text), 'html', 'utf8'))  # 邮件正文
            msg['From'] = formataddr([a, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            # print(111)
            msg['To'] = formataddr(['', email])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            # msg['Subject'] = "邮件标题"  # 邮件的主题，也可以说是标题
            msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题

            # with open('附件', 'rb') as f:
            #     mime = MIMEBase('zip', 'zip', filename='附件')
            #     # 加上必要的头信息:
            #     mime.add_header('Content-Disposition', 'attachment', filename='附件')
            #     mime.add_header('Content-ID', '<0>')
            #     mime.add_header('X-Attachment-Id', '0')
            #     # 把附件的内容读进来:
            #     mime.set_payload(f.read())
            # encoders.encode_base64(mime)
            # msg.attach(mime)
            # print('3333')
            server = smtplib.SMTP_SSL("smtp.th.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            # print('44444')
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            # print('555')
            server.sendmail(my_sender, email, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            print(i, email, '发送成功')
            i = i + 1
            server.quit()  # 关闭连接
        except Exception as err:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print(err)
            print(i,email, '发送失败')
            i= i +1
            ret = False

a = '发件人邮箱　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　···'
# a = 'admin'#使用unicode编码中无法显示出来的符号来填充
mail(a)
