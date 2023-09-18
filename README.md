# Django-SendMail

วิธีการทำให้เว็บของเราส่งข้อความผ่าน Gmail <br>

อันดับแรก อีเมลล์ที่เราใช้นั้นจะต้องเปิดการยืนยันตัวตนสองขั้นตอนแล้ว <br>
ไปที่ >หน้าจัดการบัญชี>ความปลอดภัย แล้วกดเข้าไปที่ >การยืนยันตัวตน2ขั้นตอน จากนั้นล็อกอิน <br>
เมื่อเสร็จแล้วให้เลื่อลงไปด้านล่างสุด และกดลูกศรตรงคำว่า >รหัสผ่านสำหรับแอป ที่อยู่ด้านขวาสุด <br>
จากนั้นเว็บจะให้เราตั้งชื่อ เราจะตั้งว่าอะไรก็ได้ เช่น รหัสสำหรับ 'Django' แล้วกด 'สร้าง' <br>
จะมีรหัสเด้งขึ้นมา ให้เราคัดลอกไว้ แล้วจากในไหนก็ได้ที่คิดว่าจะคัดลอกได้อีกรอบ <br>

จากนั้นไปที่ไฟล์ 'setting.py' แล้วก็อปโค้ดนี้ไปวาง <br>
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" <br>
EMAIL_HOST = "smtp.gmail.com" <br>
EMAIL_USE_TLS = True <br>
EMAIL_USE_SSL = False <br>
EMAIL_PORT = 587 <br>
EMAIL_HOST_USER = "ัอีเมลล์ของคุณ" <br>
EMAIL_HOST_PASSWORD = "รหัสที่คัดลอกไว้" <br>

จากนั้นใช้เราสร้างไฟล์(python)สักอันนึงไว้ในโฟล์เดอร์แอป และวางโค้ดนี้ได้เลย (ผมตั้งว่า sendgmail.py) <br>

from django.core.mail import send_mail <br>
from mysite.settings import EMAIL_HOST_USER <br>
def send_email_to(email, subject, message): <br>
    subject = "test mail"__
    message = "test send from django" <br>
    to_email = "" <br>
    send_mail(subject, message, EMAIL_HOST_USER, to_email, fail_silently=True) <br>
    print('mail send') <br>

จากจะเรียกใช้ใน views.py ให้อิมพอร์ตตัวนี้เข้ามาด้วย <br>
from .sendgmail import * <br>

เวลาเรียกใช้ก็ประมาณนี้ <br>
send_email_to('เมลล์ปลายทาง', 'หัวข้อ', 'เนื้อหา') <br>



















    
