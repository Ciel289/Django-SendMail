"""
ท่านสามารถดาวน์โหลดทั้งหมดนี้ แล้วนำไปวางไว้ในโฟล์เดรอ์ของแอพท่านได้เลย เช่น mywebsite/compay แล้ววาง
และท่านอย่าลืม 'from .sendgmail import *' ไว้บนส่วนหัวของไฟล์ views.py ด้วย

"""
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER

# ตัวอย่างการใช้งาน send_email_to('ถึงใคร', 'หัวข้อ', 'เนื้อหาภายใน')
def send_email_to(email, subject, message):
    subject = "test mail"
    message = "test send from django"
    to_email = ""
    send_mail(subject, message, EMAIL_HOST_USER, to_email, fail_silently=True)
    print('mail send')

