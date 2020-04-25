from email.mime.text import MIMEText
from email.utils import formataddr

import requests
import smtplib
from time import sleep
from lxml import etree
from redis import StrictRedis

sender = 'ling1ciel@163.com'
user = 'ling1ciel@163.com'
password = 'hyc121019'


def send_mail(to, title, url):
    ret = True
    try:
        mail_msg = """
            <p>点击查看最新消息</p>
            <p><a href="{0}">{1}</a></p>
        """.format(url, title)
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = formataddr(["夏尔的实验室", sender])
        message['Subject'] = '燕大研招办最新消息|夏尔的实验室'

        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(user=user, password=password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, to, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


def yzb_zxxx():
    with StrictRedis(host='39.107.25.30', port=6379, db=0, password='123456') as redis:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
        }
        while True:
            response = requests.get("https://zsjyc.ysu.edu.cn/ssszsxxw/zxxx.htm", headers=headers)
            html = etree.HTML(response.content.decode('utf-8'))
            trs = html.xpath("//tr[@class='list1']")
            for tr in trs:
                title = str(tr.xpath("td/a/text()")[0])
                url = str(tr.xpath("td/a/@href")[0])
                if not redis.sismember('yzb:zxxx_url', url):
                    # 保存数据到redis中
                    redis.sadd('yzb:zxxx_title', title)
                    redis.sadd('yzb:zxxx_url', url)

                    # 发送邮件
                    try:
                        url = "https://zsjyc.ysu.edu.cn" + url.split("..")[-1]
                        receivers = [to.decode('utf-8') for to in redis.smembers('yzb:zxxx_to')]
                        if send_mail(to=receivers, title=title, url=url):
                            print("发送成功")
                        else:
                            print("发送失败")
                    except smtplib.SMTPException:
                        print("Error: 无法发送邮件")
            sleep(5 * 60)


if __name__ == '__main__':
    yzb_zxxx()
