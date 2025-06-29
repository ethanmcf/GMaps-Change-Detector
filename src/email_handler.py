import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email():
    EMAIL_RECIPIENTS = os.environ.get("EMAIL_RECIPIENTS").split(",")
    SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
    SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
    SMTP_SERVER = os.environ.get("SMTP_SERVER")
    SMTP_PORT = os.environ.get("SMTP_PORT")

    msg = EmailMessage()
    msg['Subject'] = "GMAPS ALERT: Majestic Elegance Costa Mujeres has been updated"
    msg['From'] = SENDER_EMAIL
    msg['To'] = EMAIL_RECIPIENTS
    content = """
    Majestic Elegance Costa Mujeres has been updated.

    See screenshot below or click google maps link below.

    https://www.google.com/maps/place/Majestic+Elegance+Costa+Mujeres/@21.2811059,-86.8200595,1083m/data=!3m2!1e3!4b1!4m9!3m8!1s0x8f4c318a57aa36e7:0xc3ed13366f9e5d55!5m2!4m1!1i2!8m2!3d21.2811059!4d-86.8200595!16s%2Fg%2F11h07gcl3z?entry=ttu&g_ep=EgoyMDI1MDYyMy4yIKXMDSoASAFQAw%3D%3D
    """
    msg.set_content(content)
    with open('src/screenshots/recent.png', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
    print("Email sent")