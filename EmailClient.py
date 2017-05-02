# Python Email Client
# Made by Isaac Delly

import shelve
import smtplib
from imapclient import IMAPClient
import imapclient
from backports import ssl
import time
import pyzmail
import os

print('Python Email Client')
print('\nWARNING: ALL DATA IS UNENCRYPTED')

try:
    user = shelve.open('mydata')
    address = user['email'][0]
    smtp = user['email'][1]
    password = user['email'][2]
    
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
    
def readAll():
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        server = imapclient.IMAPClient(smtp, ssl = True, ssl_context = context)
        server.login(address, password)
        server.select_folder('INBOX', readonly = True)
        UID = server.search(['SEEN'])
        print('\nYou have ' + str(len(UID)) + ' emails being queried\n')
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        x = (len(UID) - 10)
        i = len(UID)
        while (i > x):
            i -= 1
            var = UID[i]
            rawMessage = server.fetch(UID[i], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[var][b'BODY[]'])
            subject = message.get_subject()
            sender = message.get_address('from')
            receiver = message.get_address('to')
            if (message.text_part == None):
                print('\n\nError locating UID [' + str(i) + ']\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            if (message.text_part.charset == None):
                print('\n\nError locating UID [' + str(i) + ']\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            print('\n\n[' + str(i) + ']')
            print('SUBJECT: ' + str(subject))
            print('SENT BY: ' + str(sender))
            os.environ["LANG"]="en_US.UTF-8"
            message.text_part != None
            os.environ["LANG"]="en_US.UTF-8"
            print('\nMESSAGE: \n'+ str(message.text_part.get_payload().decode(message.text_part.charset)))
            print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if (i == x):
                print('Enter "+" to read more emails')
                print('Enter "exit" to exit')
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
        UID = server.search(['UNSEEN'])
        print('\nYou have ' + str(len(UID)) + ' emails being queried\n')
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        x = (len(UID) - 10)
        i = len(UID)
        while (i > x):
            i -= 1
            var = UID[i]
            rawMessage = server.fetch(UID[i], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[var][b'BODY[]'])
            subject = message.get_subject()
            sender = message.get_address('from')
            receiver = message.get_address('to')
            if (message.text_part == None):
                print('\n\nError locating UID [' + str(i) + ']\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            if (message.text_part.charset == None):
                print('\n\nError locating UID [' + str(i) + ']\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            print('\n\n[' + str(i) + ']')
            print('SUBJECT: ' + str(subject))
            print('SENT BY: ' + str(sender))
            message.text_part != None
            os.environ["LANG"]="en_US.UTF-8"
            print('\nMESSAGE: \n'+ str(message.text_part.get_payload().decode(message.text_part.charset)))
            print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if (i == x):
                print('Enter "+" to read more emails')
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
        print('\nYou have ' + str(len(UID)) + ' emails being queried\n')
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        x = (len(UID) - 10)
        i = len(UID)
        while (i > x):
            i -= 1
            var = UID[i]
            rawMessage = server.fetch(UID[i], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[var][b'BODY[]'])
            subject = message.get_subject()
            sender = message.get_address('from')
            receiver = message.get_address('to')
            if (message.text_part == None):
                print('\n\nError locating UID [' + str(i) + ']\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            if (message.text_part.charset == None):
                print('\n\nError locating UID [' + str(i) + ']\n\n')
                print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                continue
            print('\n\n[' + str(i) + ']')
            print('SUBJECT: ' + str(subject))
            print('SENT BY: ' + str(sender))
            message.text_part != None
            os.environ["LANG"]="en_US.UTF-8"
            print('\nMESSAGE: \n'+ str(message.text_part.get_payload().decode(message.text_part.charset)))
            print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if (i == x):
                print('Enter "+" to read more emails')
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
    try:
        print('Enter recipient:')
        recipient = input()
        print('Enter subject:')
        subject = 'Subject: ' + input() + '\r\n'
        print('Enter body:')
        body = subject + input()
        server = smtplib.SMTP(smtp, 587)
        server.ehlo()
        server.starttls()
        server.login(address, password)
        server.sendmail(address, recipient, body)
        server.quit()
        print('\nEmail sent successfully')
        
    except Exception as e:
        print('\nAn error ocurred: ' + str(e) )

while True:
    print('\nWould you like to send or read an email?')
    print('Enter send() to send')
    print('Enter read() to view only unread emails')
    print('Enter readAll() to view a range of read emails')
    print('Enter logout() to delete your saved data and exit this module')
    if smtp == 'smtp.gmail.com':
        print('Enter search() to query an email by string\n')
    prompt = input()
    if prompt == 'send()':
        send()
    elif prompt == 'read()':
        read()
    elif prompt == 'readAll()':
        readAll()
    elif prompt == 'logout()':
        logout()
    elif prompt == 'search()':
        search()
