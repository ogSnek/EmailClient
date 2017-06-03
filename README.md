# EmailClient
# Isaac Delly

EmailClient.py is a Python project that connects to a user's SMTP account and allows to send, receive, and index emails

This project requires Python 3+ to operate

CONCEPT:

Program first indexes 'mydata.dat' for possible saved SMTP account information

If no data is found then the user is prompted to enter an SMTP email and password that will then be saved into maydata.dat to be referenced for later sessions

Functions to call:
logout = Wipes mydata.dat information and close session
readAll = Indexes all received emails in Inbox
read = Indexes only unread emails
search = Prompts user for a string that will be queried and will return any emails found 
send = Sends a message to a directed receiver

Trouble Shooting FAQ:
If "An error ocurred" is printed, it is possible that you entered your email/password wrong and is denied by the SMTP server. Try the logout() function to logout and login again.

if "Error locating UID [#] Text type not supported" is returned when read, readAll, or search is called, then the email body being queried is not adapted to this program. This is a bug that is currently being fixed.
