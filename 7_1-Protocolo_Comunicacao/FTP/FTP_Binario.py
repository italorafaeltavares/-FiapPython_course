from ftplib import *
ftp = FTP('ftp.ibiblio.org')            # Cria a conexão FTP
print(ftp.getwelcome())
ftp.login()                             # Estabelexe login    
ftp.cwd('/pub/linux/logos/pictures')    # Define diretório

with open ('pai_do_linus.jpg', 'wb') as arq
    ftp.retrbinary('RETR linus-father-of-linus.jpg', arq.write)

ftp.quit()
