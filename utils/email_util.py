import random
from _md5 import md5
from threading import Thread

from django.urls import reverse

from django.core.mail import send_mail
from django.template.loader import render_to_string
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature, BadData

from home.models import ContactEmail
from web.settings import EMAIL_FROM


def get_random_code(n):
    code = ''  # 拼接随机生成的数字或字母
    for i in range(0, n):
        '''循环n次生成n个字母或数字'''
        # 生成数字
        # 注意：将数字转换成字符串
        num = str(random.randint(0, 9))
        # 生成字母  ASC码A:65~z:90
        zm = chr(random.randint(65, 90))
        # 随机产生一个内容
        ret = random.choice([num, zm])
        code += ret  # 把code和ret用空字符串拼接
    return code


def get_random_salt(n):
    md5_obj = md5()
    md5_obj.update(get_random_code(n).encode('utf8'))
    return md5_obj.hexdigest()


def generate_token(key, code, expiration=600):
    s = Serializer(secret_key=SECRET_KEY, salt=AUTH_SALT, expires_in=expiration)
    return s.dumps({'key': key, 'code': code}).decode(encoding='utf-8')


def parse_token(token):
    s = Serializer(secret_key=SECRET_KEY, salt=AUTH_SALT)
    try:
        data = s.loads(token)
        return data.get('key'), data.get('code')
    except SignatureExpired:
        msg = 'token expired'
        return msg
    except BadSignature as e:
        encoded_payload = e.payload
        if encoded_payload is not None:
            try:
                s.load_payload(encoded_payload)
            except BadData:
                msg = 'token tampered'
                return msg
        msg = 'badSignature of token'
        return msg


def send_async_email(subject, message, from_email, recipient_list):
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


def send_contact_mail(nickname, email, message):
    try:
        ContactEmail.objects.create(nickname=nickname, email=email, message=message)
        send_mail("来自主页【联系我】的邮件", message, EMAIL_FROM, ['1102839480@qq.com'])
        # thread = Thread(target=send_async_email, args=["来自主页【联系我】的邮件", message, EMAIL_FROM, ['1102839480@qq.com']])
        # thread.start()
        return True
    except Exception as e:
        return False


def send_code_mail(to, _type):
    e = EmailVerifyCode.objects.create(email=to, type=_type, code=get_random_code(6))
    title = '【来自 ** 的验证码】'
    msg = render_to_string(template_name='email_sms.html', context={'code': e.code})
    if _type == 1:
        title += '欢迎注册'
        token = generate_token(to, code=e.code)
        url = reverse('users:email_validate') + token
        msg = render_to_string(template_name='email_validate.html', context={'url': url})
    elif _type == 2:
        title += '忘记密码'
    else:
        title += '更换邮箱'
    status = send_mail(title, '', EMAIL_FROM, [to], html_message=msg)
    if status:
        return True
    else:
        return False
