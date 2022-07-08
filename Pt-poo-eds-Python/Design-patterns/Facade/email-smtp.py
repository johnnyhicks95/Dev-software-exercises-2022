"""
It would be nice to have a simple class that allows us to send a single e-mail, and 
list the e-mails currently in the inbox on an IMAP or POP3 connection. To keep our 
example short, we'll stick with IMAP and SMTP: two totally different subsystems 
that happen to deal with e-mail. Our facade performs only two tasks: sending an 
e-mail to a specific address, and checking the inbox on an IMAP connection. I
"""
import smtplib
import imaplib

class EmailFacade:
    def __init__( self, host, username, password ):
        self.host = host
        self.username = username
        self.password = password
        
    def send_email( self, to_email, subject, message ):
        """The send_email method formats the e-mail address 
        and message, and sends it using smtplib."""
        if not "@" in self.username:
            from_email = "{0}@{1}".format( self.username, self.host )
        else:
            from_email = self.username
        message = ( "From: {0}\r\n" 
                   "To: {1}\r\n"
                   "subject: {2}\r\n\r\n{3} "
                   ).format(
                       from_email,
                       to_email,
                       subject,
                       message
                   )
                   
        smtp = smtplib.SMTP( self.host )
        smtp.login( self.username, self.password )
        smtp.sendmail( from_email, [to_email], message )

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login( bytes(self.username, 'utf8'), bytes(self.password, 'utf8') )
        mailbox.select()
        x, data = mailbox.search( None, 'ALL' )
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch( num, 'RFC822' )
            messages.append(message[0][1])
        return messages
            
        
