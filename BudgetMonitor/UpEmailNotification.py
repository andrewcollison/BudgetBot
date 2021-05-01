import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

import smtplib

class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)




def main():
    load_dotenv('UpBankApp.env')
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')

    html_message = '''<body style="margin: 0; padding: 0;">
    <table role="presentation" border="1" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td>
                <p style="margin: 0;">Hello!</p>
            </td>
        </tr>
    </table>
</body> '''
    gm = Gmail(email_user, email_pass)
    gm.send_message('howdy Cowboy', html_message)

if __name__ == "__main__":
    main()



