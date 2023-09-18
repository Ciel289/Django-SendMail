# Django-SendMail

วิธีการทำให้เว็บของเราส่งข้อความผ่าน Gmail

อันดับแรก อีเมลล์ที่เราใช้นั้นจะต้องเปิดการยืนยันตัวตนสองขั้นตอนแล้ว
ไปที่ >หน้าจัดการบัญชี>ความปลอดภัย แล้วกดเข้าไปที่ >การยืนยันตัวตน2ขั้นตอน จากนั้นล็อกอิน 
เมื่อเสร็จแล้วให้เลื่อลงไปด้านล่างสุด และกดลูกศรตรงคำว่า >รหัสผ่านสำหรับแอป ที่อยู่ด้านขวาสุด
จากนั้นเว็บจะให้เราตั้งชื่อ เราจะตั้งว่าอะไรก็ได้ เช่น รหัสสำหรับ 'Django' แล้วกด 'สร้าง'
จะมีรหัสเด้งขึ้นมา ให้เราคัดลอกไว้ แล้วจากในไหนก็ได้ที่คิดว่าจะคัดลอกได้อีกรอบ

จากนั้นไปที่ไฟล์ 'setting.py' แล้วก็อปโค้ดนี้ไปวาง
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = "ัอีเมลล์ของคุณ"
EMAIL_HOST_PASSWORD = "รหัสที่คัดลอกไว้"

จากนั้นใช้เราสร้างไฟล์(python)สักอันนึงไว้ในโฟล์เดอร์แอป และวางโค้ดนี้ได้เลย (ผมตั้งว่า sendgmail.py)

from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
def send_email_to(email, subject, message):
    subject = "test mail"
    message = "test send from django"
    to_email = ""
    send_mail(subject, message, EMAIL_HOST_USER, to_email, fail_silently=True)
    print('mail send')

จากจะเรียกใช้ใน views.py ให้อิมพอร์ตตัวนี้เข้ามาด้วย
from .sendgmail import * 

เวลาเรียกใช้ก็ประมาณนี้
send_email_to('เมลล์ปลายทาง', 'หัวข้อ', 'เนื้อหา')



















    
