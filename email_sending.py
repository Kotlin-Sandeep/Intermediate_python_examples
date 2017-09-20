import sys, smtplib

fromaddr = raw_input("From: ")
toaddrs  = raw_input("To: ").split(',')
print("Enter message, ends with ^D: ")
msg = ''
while True:
    line = sys.stdin.readline()
    if not line:
        break
    msg +=line
server = smtplib.SMTP('127.0.0.1')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
