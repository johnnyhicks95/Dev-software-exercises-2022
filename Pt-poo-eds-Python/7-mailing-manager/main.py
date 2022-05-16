""" 
Python has our back here; like the test HTTP server, it has a built-in Simple Mail Transfer Protocol
(SMTP) server that we can instruct to capture any messages we send without 
actually sending them. We can run the server with the following command:

python -m smtpd -n -c DebuggingServer localhost:1025
 """


import smtplib
from email.mime.text import MIMEText

def send_email( subject, message, from_addr, *to_addrs,
               host="localhost", port=1025, headers=None ):
    #  if headrs is None else headers
    headers= {}
    
    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    for header, value in header.items():
        email[header] = value
        
    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email["To"]
        email["To"] = addr
        sender.sendmail( from_addr, addr, email.as_string() )
    sender.quit()


""" Since the values in our dictionary will always be collections of unique e-mail 
addresses, we should probably store them in a set container. We can use 
defaultdict to ensure that there is always a set container available for each key:3
 """

from collections import defaultdict

class MailingList:
    # Manage groups of e-mail addresses for sending e-mails
    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)
        
    def add_to_group( self, email, group ):
        self.email_map[email].add(group)
        
    # Collect in one or more groups
    def emails_in_groups( self, *groups ):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

# Sending emails to specific groups
    def send_mailing( self, subject, message, from_addr,
                     *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email( subject, message, from_addr,
                   *emails, headers=headers)
 
#  Saving files in a document, formatted string
def save(self):
    with open(self.data_file, 'w') as file:
        for email, groups in self.email_map.items():
            file.write('{} {}\n'.format(email, ','.join(groups) ) )
def load(self):
    self.email_map = defaultdict(set)
    try:
        with open(self.data_file) as file:
            for line in file:
                email, groups = line.strip().split(' ')
                groups = set(groups.split(','))
                self.email_map[email] = groups
    except IOError:
        pass

#  API in their own code
def __enter__(self):
    self.load()
    return self

def __exit__( self, type, value, tb ):
    self.save()
 
 
"""  Executing the code:

python -i mailing_list.py

Create a MailingList object with:
>>> m = MailingList()
Then create a few fake e-mail addresses and groups, along the lines of:
>>> m.add_to_group("friend1@example.com", "friends")
>>> m.add_to_group("friend2@example.com", "friends")
>>> m.add_to_group("family1@example.com", "family")
>>> m.add_to_group("pro1@example.com", "professional")

Finally, use a command like this to send e-mails to specific groups:
>>> m.send_mailing("A Party", "Friends and family only: a party", "me@example.com", "friends",
"family", headers={"Reply-To": "me2@example.com"})
E-mails to each of the addresses in the specified groups should show up in the 
console on the SMTP server.


**Considerations
Finally, there are many security implications we 
need to consider: can someone get themselves into the wrong group by putting a fake 
comma in their e-mail address? What does the parser do if it encounters an invalid file?

 """