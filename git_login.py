import requests
import re
from parsel import Selector
import time


sess = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
}

login_url = 'https://github.com/login'


response_login = sess.get(url=login_url, headers=headers)
print(response_login.text)

print('*'*30)
response_s = Selector(response_login.text)
authenticity_token = response_s.xpath('//input[@name="authenticity_token"]/@value').get()
print(authenticity_token)
timestamp_secret = response_s.xpath('//input[@name="timestamp_secret"]/@value').get()
print(timestamp_secret)

do_login_url = 'https://github.com/session'
data = {
'commit': 'Sign in',
'authenticity_token': authenticity_token,
'login': '815583442@qq.com',  # user account
'password': '666666',  # your password
'trusted_device': '',
'webauthn-support': 'supported',
'webauthn-iuvpaa-support': 'unsupported',
'return_to': '',
'allow_signup': '',
'client_id': '',
'integration': '',
'required_field_7bf6': '',
'timestamp': str(int(time.time()*1000)),
'timestamp_secret': timestamp_secret,
}
response_l = sess.get(url=login_url, data=data, headers=headers)
print(response_l.text)

