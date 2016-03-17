import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

class SendMail():
        def __init__(self,user_name,passwd):
                self.sg = sendgrid.SendGridClient(user_name, passwd,raise_errors=True)
                self.message = sendgrid.Mail()
        def send_mail(self,rcpt,frm,subject,msg):


                self.message.add_to(rcpt)
                self.message.set_subject(subject)
                self.message.set_html(msg)
                self.message.set_text(msg)
                self.message.set_from(frm)
                try:
                        status, msg = self.sg.send(self.message)
                        return status
                except SendGridClientError:
                        return 400
                except SendGridServerError:
                        return 500
                        
                        