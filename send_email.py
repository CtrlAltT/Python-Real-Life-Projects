import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'User'
email['to'] = "user@gmail.com"
email['subject'] = 'Send a email'

email.set_content(html.substitute(name='Tim'), 'html')


with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.login('user@gmail', '123456')
    smtp.send_message(email)
    print('All done')

