#!/usr/bin/env python2.7
import urllib
from bs4 import BeautifulSoup
from datetime import datetime

def send_email(user, pwd, recipient, subject, body):
	import smtplib

	gmail_user = user
	gmail_pwd = pwd
	FROM = user
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body

	# Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() # optional, called by login()
	server_ssl.login(gmail_user, gmail_pwd)
	server_ssl.sendmail(FROM, TO, message)
	server_ssl.close()

url = 'XXX'
sock = urllib.urlopen(url)
html_page = sock.read()
sock.close()
soup_page = BeautifulSoup(html_page, 'html.parser')

new_entry = soup_page.findAll("div", { "class" : "entry unvoted" })[1]
print('NEW ENTRY')
print(new_entry)
post = new_entry.find("div", { "class" : "md" }).p.string
print('NEW POST')
print(post)
time = new_entry.find('time')['datetime']
print('TIME')
print(time)
with open('time_saved.txt', 'r') as time_saved_file:
	time_saved=time_saved_file.read()
	if(time != time_saved):
		send_email('XXX', 'XXX', 'XXX', 'XXX', post)
	else:
		print('NO NEW POST')
with open("time_saved.txt", "w") as time_saved_file:
	time_saved_file.write(time)