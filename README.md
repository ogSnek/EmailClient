# EmailClient

EmailClient connects to a user's SMTP account and allows to send, receive, and index emails fluidly and efficiently.

# Installation

Required Python 3+

Clone repo: `$ git clone https://github.com/Isaacdelly/EmailClient`

<br/>

Install Requirements: 

```
pip install -r requirements.txt
```


#

# Concept

EmailClient.py is a Python project that connects to a user's SMTP account and allows to send, receive, and index emails. </br>
<br/>
Program first indexes 'mydata.dat' for possible saved SMTP account information.<br/>
<br/>
If no data is found then the user is prompted to enter an SMTP email and password that will then be saved into maydata.dat to be referenced for later sessions.<br/>
<br/>
The program connects to the STMP server associated with the user's email, and queries information based on the specific input.<br/>
<br/>

<b>Functions to call: </b><br/>

`logout` = Wipes mydata.dat information and close session<br/>
`readAll` = Indexes all received emails in Inbox<br/>
`read` = Indexes only unread emails<br/>
`search` = Prompts user for a string that will be queried and will return any emails found <br/>
`send` = Sends a message to a directed receiver<br/>

#

# Trouble Shooting FAQ:

If `An error ocurred` is printed, it is possible that you entered your email/password wrong and is denied by the SMTP server. Try the logout() function to logout and login again.

if `Error locating UID [#] Text type not supported` is returned when read, readAll, or search is called, then the email body being queried is not adapted to this program. Pyzmail is depreciated when encountering certian text types.
