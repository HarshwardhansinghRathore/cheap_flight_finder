import smtplib

class NotificationManager:
    def __init__(self):
        self.mail_id = 'hr1566027@gmail.com'
        self.app_password = 'brodlyeytybyjwdx'

    def send_mail(self, message):
        connection = smtplib.SMTP('smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=self.mail_id, password=self.app_password)
        connection.sendmail(from_addr=self.mail_id,
                            to_addrs='hrathore076@gmail.com',
                            msg=f'Subject:cheap flight deals\n\n{message}')
        connection.close()
