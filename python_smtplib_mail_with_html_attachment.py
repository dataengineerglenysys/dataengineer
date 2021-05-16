import yaml
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open("python_smtplib_mail_with_html_attachment_cfg.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)
	
username = cfg['username']
password = cfg['password']
From = username
To = cfg['To']

try:
    df = pd.read_csv("data_region.csv") # creating dataframe
    df_html = df.to_html() # converting dataframe to html
    df_attach_html = MIMEText(df_html,'html')
    # msg container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'May16th - Region wise sales data'
    msg.attach(df_attach_html)
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(From, To, msg.as_string())
    server.close()
    print('Email sent successfully')
except smtplib.SMTPException:
   print("Error: unable to send email")