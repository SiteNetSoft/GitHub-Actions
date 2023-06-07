import ftplib
import os
import glob

server = os.getenv('FTP_SERVER')
username = os.getenv('FTP_USERNAME')
password = os.getenv('FTP_PASSWORD')

ftp = ftplib.FTP(server)
ftp.login(user=username, passwd=password)

files = glob.glob('myfiles/*')

for file in files:
    with open(file, 'rb') as f:
        ftp.storbinary('STOR ' + file, f)

ftp.quit()