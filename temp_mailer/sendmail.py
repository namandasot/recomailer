import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

class SendMail():
        def __init__(self,user_name,passwd):
                self.sg = sendgrid.SendGridClient(user_name, passwd,raise_errors=True)
                self.message = sendgrid.Mail()
        def send_mail(self,rcpt,frm,subject,msg):

                """
                        send_mail sends mail from GCE
                        Arguments req :
                                rcpt : a list of name and email ex :
                                        ['Ravi <ravi.manik@innovaccer.com>','Ankit <ankit.maheshwari@innovaccer.com>']
                                subject : "Subject of the mail"
                                msg: "Body of the mail"
                                frm: "from takes name a email" ex: 'Ravi <ravi.manik@innovaccer.com>''

                                returns:
                                        http_status_code
                                                when exception is caught returns 400 or 500

                """

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
                        
                        