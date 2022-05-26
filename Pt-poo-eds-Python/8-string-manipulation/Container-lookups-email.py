""" Using non primitive complex objects like list or dictionaries, or tuples can be
accesed too trough indexes  """

emails = ("a@example.com","b@example.com")
message = {
    'subject': "You have a mail",
    'message': "Here's some email for you"
}
template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}
"""
print(template.format(emails, message=message))

