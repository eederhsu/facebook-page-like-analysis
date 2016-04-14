#coding=utf-8
import smtplib
from email.mime.text import MIMEText

def send_email(message,subject,toaddrs):

    fromaddr = 'thepowerfulest@gmail.com'
    username = 'thepowerfulest'
    password = 'trytrysee'
    
    
    msg = MIMEText(message, 'html')
    
    msg['Subject']  = subject
    
    msg['From']=fromaddr
    
    msg['Reply-to'] = 'no-reply'
    
    msg['To'] = toaddrs
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    server.starttls()
    
    server.login(username,password)
    
    server.sendmail(fromaddr, [toaddrs], msg.as_string())
    server.quit()
    print('success in '+subject)
   


#subject = 'cool' #raw_input("Enter your subject?\n")
#message = 'Find it' #raw_input("Enter your mesage?\n")
#toaddrs = 'w19940503@gmail.com' #raw_input("Enter receiver email address?\n")
#send_email(str(message),str(subject),str(toaddrs))
