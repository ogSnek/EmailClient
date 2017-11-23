# Python Email Client
# Made by Isaac Delly
# https://github.com/Isaacdelly/EmailClient

import shelve
import smtplib
from imapclient import IMAPClient
import imapclient
from backports import ssl
import time
import pyzmail
import os

print('Python Email Client')

try:
    user = shelve.open('mydata')
    address = user['email'][0]
    smtp = user['email'][1]
    password = user['email'][2]
# Try to read from a saved data file
# If nothing is found run except

except:
    print('\nLOGIN:\n')
    print('Email Address:')
    address = input()
    print('Password:')
    password = input()
    if '@gmail' in address:
        smtp = 'smtp.gmail.com'
    elif '@outlook' or 'hotmail' in address:
        smtp = 'smtp-mail.outlook.com'
    elif '@yahoo' in address:
        smtp = 'smtp.mail.yahoo.com'
    user = shelve.open('mydata')
    email = [address, smtp, password]
    user['email'] = email
    print('User information stored in \'mydata.dat\'')
# Ask for information and save to data file to be retrieved later

def logout():
    with open('mydata.dat', 'w'):
        pass
    with open('mydata.bak', 'w'):
        pass
    with open('mydata.dir', 'w'):
        pass
    user.close()
    print('\nUser information deleted')
    time.sleep(1)
    exit()
# Erase data file and relatives and end program
    
def readAll():
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        server = imapclient.IMAPClient(smtp, ssl = True, ssl_context = context)
        server.login(address, password)
        server.select_folder('INBOX', readonly = True)  # Read from Inbox
        UID = server.search(['SEEN'])
        x = (len(UID) - 10) # Only print 10 emails at a time
        i = len(UID)
        if (i > 0): # Print number of emails found
            print('\nYou have ' + str(len(UID)) + ' emails being queried\n')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if (i == 0):
            print('\nYou have no new mail\n')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        while ( (i > x) and (i > 0) ):
            i -= 1
            var = UID[i]  # If an email is found, parse through it
            rawMessage = server.fetch(UID[i], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[var][b'BODY[]'])
            subject = message.get_subject()
            sender = message.get_address('from')
            receiver = message.get_address('to')
            if (message.text_part == None):
                print('\n\nError loading UID [' + str(i) + ']\n\nText type not supported\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            if (message.text_part.charset == None):
                print('\n\nError loading UID [' + str(i) + ']\n\nText type not supported\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            print('\n\n[' + str(i) + ']') # Print the parsed email's body
            print('SUBJECT: ' + str(subject))
            print('SENT BY: ' + str(sender))
            os.environ["LANG"]="en_US.UTF-8"
            message.text_part != None
            os.environ["LANG"]="en_US.UTF-8"
            print('\nMESSAGE: \n'+ str(message.text_part.get_payload().decode(message.text_part.charset)))
            print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if (i == x):
                print('Enter "+" to read more emails')
                print('Enter "exit" to exit') # Prompt user to load more emails
                prompt = input()
                if prompt == '+':
                    x -= 10
                elif prompt == 'stop':
                    x += 100
                    
    except Exception as e:
        print('An error occured: ' + str(e))
        print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def read():
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        server = imapclient.IMAPClient(smtp, ssl = True, ssl_context = context)
        server.login(address, password)
        server.select_folder('INBOX', readonly = False)
        UID = server.search(['UNSEEN']) # Read only unseen emails
        x = (len(UID) - 10) # Only print 10 emails at a time
        i = len(UID)
        if (i > 0): # Print number of emails found
            print('\nYou have ' + str(len(UID)) + ' emails being queried\n')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if (i == 0):
            print('\nYou have no new mail\n')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        while ( (i > x) and (i > 0) ):
            i -= 1
            var = UID[i] # If an email is found parse through it
            rawMessage = server.fetch(UID[i], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[var][b'BODY[]'])
            subject = message.get_subject()
            sender = message.get_address('from')
            receiver = message.get_address('to')
            if (message.text_part == None):
                print('\n\nError loading UID [' + str(i) + ']\n\nText type not supported\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            if (message.text_part.charset == None):
                print('\n\nError loading UID [' + str(i) + ']\n\nText type not supported\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            print('\n\n[' + str(i) + ']') # Print parsed email's body
            print('SUBJECT: ' + str(subject))
            print('SENT BY: ' + str(sender))
            message.text_part != None
            os.environ["LANG"]="en_US.UTF-8"
            print('\nMESSAGE: \n'+ str(message.text_part.get_payload().decode(message.text_part.charset)))
            print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if (i == x):
                print('Enter "+" to read more emails') # Prompt user t0 load more emails
                print('Enter "exit" to exit')
                prompt = input()
                if prompt == '+':
                    x -= 10
                elif prompt == 'stop':
                    x += 100
                    
    except Exception as e:
        print(str(e))
        print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def search():
    try:
        print('Enter string to search for: ')
        phrase = input()
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        server = imapclient.IMAPClient(smtp, ssl = True, ssl_context = context)
        server.login(address, password)
        server.select_folder('INBOX', readonly = True)
        UID = server.gmail_search(str(phrase))
        x = (len(UID) - 10) # Only print 10 emails at a time
        i = len(UID)
        if (i > 0): # Print number of emails found
            print('\nYou have ' + str(len(UID)) + ' emails being queried\n')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if (i == 0):
            print('\nYou have no new mail\n')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        while ( (i > x) and (i > 0) ):
            i -= 1
            var = UID[i] # If an email is found parse through it
            rawMessage = server.fetch(UID[i], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[var][b'BODY[]'])
            subject = message.get_subject()
            sender = message.get_address('from')
            receiver = message.get_address('to')
            if (message.text_part == None):
                print('\n\nError locating UID [' + str(i) + ']\n\nText type not supported\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            if (message.text_part.charset == None):
                print('\n\nError locating UID [' + str(i) + ']\n\nText type not supported\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            print('\n\n[' + str(i) + ']')# Print parsed email's body
            print('SUBJECT: ' + str(subject))
            print('SENT BY: ' + str(sender))
            message.text_part != None
            os.environ["LANG"]="en_US.UTF-8"
            print('\nMESSAGE: \n'+ str(message.text_part.get_payload().decode(message.text_part.charset)))
            print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if (i == x):
                print('Enter "+" to read more emails') # Prompt user to load more emails
                print('Enter "exit" to exit')
                prompt = input()
                if prompt == '+':
                    x -= 10
                elif prompt == 'stop':
                    x += 100
                    
    except Exception as e:
        print(str(e))
        print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
def send():
    try: # Enter required info
        print('Enter recipient:')
        recipient = input()
        print('Enter subject:')
        subject = 'Subject: ' + input() + '\r\n'
        print('Enter body:')
        body = subject + input()
        server = smtplib.SMTP(smtp, 587) # Connect to server and send email
        server.ehlo()
        server.starttls()
        server.login(address, password)
        server.sendmail(address, recipient, body)
        server.quit()
        print('\nEmail sent successfully')
        
    except Exception as e:
        print('\nAn error ocurred: ' + str(e) )

while True: # Prompt user for action
    print('\nWould you like to send or read an email?')
    print('Enter \'send\' to send')
    print('Enter \'read\' to view only unread emails')
    print('Enter \'readAll\' to view a range of read emails')
    print('Enter \'logout\' to delete your saved data and exit this module')
    if smtp == 'smtp.gmail.com':
        print('Enter \'search\' to query an email by string\n')
    prompt = input()
    if prompt == 'send':
        send()
    elif prompt == 'read':
        read()
    elif prompt == 'readAll':
        readAll()
    elif prompt == 'logout':
        logout()
    elif prompt == 'search':
        search()

