import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os

load_dotenv()

conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
sender = os.getenv("MYEMAIL")
receiver = os.getenv("MYEMAIL")
subject = 'Italian Consulate Passport bot'

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver


def sendAlert(name, message):
    """Baisc email containing plain text scraped from the Consulate website and an image of the final page"""
    msg.attach(MIMEText(message, 'plain'))
    with open(f'./{name}', 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name="screenshot.png")
    msg.attach(image)
    conn.starttls()
    conn.login(os.getenv("MYEMAIL"), os.getenv("EMAILPW"))
    conn.sendmail(sender, receiver, msg.as_string())
    conn.quit()
