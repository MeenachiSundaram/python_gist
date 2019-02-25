
## one line command
python -c "import smtplib; server = smtplib.SMTP('mail_server'); server.sendmail('from', 'to', 'Subject: what\r\nhello'); server.quit()"

## To find mail server
# nslookup -query=mx DNS_Record # bash command
