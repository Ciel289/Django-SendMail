# Django-SendMail

วิธีการทำให้เว็บของเราส่งข้อความผ่าน Gmail__

อันดับแรก อีเมลล์ที่เราใช้นั้นจะต้องเปิดการยืนยันตัวตนสองขั้นตอนแล้ว__
ไปที่ >หน้าจัดการบัญชี>ความปลอดภัย แล้วกดเข้าไปที่ >การยืนยันตัวตน2ขั้นตอน จากนั้นล็อกอิน <br>
เมื่อเสร็จแล้วให้เลื่อลงไปด้านล่างสุด และกดลูกศรตรงคำว่า >รหัสผ่านสำหรับแอป ที่อยู่ด้านขวาสุด <br>
จากนั้นเว็บจะให้เราตั้งชื่อ เราจะตั้งว่าอะไรก็ได้ เช่น รหัสสำหรับ 'Django' แล้วกด 'สร้าง' <br>
จะมีรหัสเด้งขึ้นมา ให้เราคัดลอกไว้ แล้วจากในไหนก็ได้ที่คิดว่าจะคัดลอกได้อีกรอบ__

จากนั้นไปที่ไฟล์ 'setting.py' แล้วก็อปโค้ดนี้ไปวาง__
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"__
EMAIL_HOST = "smtp.gmail.com"__
EMAIL_USE_TLS = True__
EMAIL_USE_SSL = False__
EMAIL_PORT = 587__
EMAIL_HOST_USER = "ัอีเมลล์ของคุณ"__
EMAIL_HOST_PASSWORD = "รหัสที่คัดลอกไว้"__

จากนั้นใช้เราสร้างไฟล์(python)สักอันนึงไว้ในโฟล์เดอร์แอป และวางโค้ดนี้ได้เลย (ผมตั้งว่า sendgmail.py)__

from django.core.mail import send_mail__
from mysite.settings import EMAIL_HOST_USER__
def send_email_to(email, subject, message):__
    subject = "test mail"__
    message = "test send from django"__
    to_email = ""__
    send_mail(subject, message, EMAIL_HOST_USER, to_email, fail_silently=True)__
    print('mail send')__

จากจะเรียกใช้ใน views.py ให้อิมพอร์ตตัวนี้เข้ามาด้วย__
from .sendgmail import * __

เวลาเรียกใช้ก็ประมาณนี้__
send_email_to('เมลล์ปลายทาง', 'หัวข้อ', 'เนื้อหา')__



















    
