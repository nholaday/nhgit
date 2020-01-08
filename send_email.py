import smtplib
EMAIL_ADDRESS = '@gmail.com'
PASSWORD = ''

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, "nic.holaday@comfyapp.com", message)
        server.quit()
    except:
        print("Email failed to send.")
        raise

if __name__ == "__main__":
    send_email('test subject', 'test message')