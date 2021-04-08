#! /usr/bin/python3

'''
This is to send an email via smtp
'''

import socket
import urllib.request as request
import smtplib
from email.message import EmailMessage
import time
import json

try:
    f = open("./env/email.json")     # get your information
    data = json.load(f)
    email = data['email']
    pwd = data['auth_code']
    server = data['server']
    receiver = data['receiver']
except Exception as e:
    print(e)
    exit 

#Send an email
def send_email(text):
    try:
        msg = EmailMessage()
        msg.set_content('My IP address is:'+text)
        msg['Subject'] = 'IP Address of Raspberry PI'
        msg['From'] = email
        msg['To'] = receiver
    
        s = smtplib.SMTP(server)
        s.login(email, pwd)
        s.send_message(msg)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
        
#Get host ip
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

#Check network
def check_network():
    status = False
    for _ in range(0, 5):
        try:
            request.urlopen('https://google.com').read()
            print('Network is ready!')
            status = True
            break
        except Exception as e:
            print(e)
            print('Network is not ready, sleep 5 seconds')
            time.sleep(5)
    
    if status:
        return True
    else:
        return False
        
if __name__ == '__main__':
    if check_network():
        ip_address = get_host_ip()
        print('My ip is:'+ip_address)
        if send_email(ip_address):
            print('Success!')
        else:
            print('Failure!')
    else:
        print('Sorry that network does not work')
    