import re

def CheckValidMail(mail):
    pattern = '([0-9a-zA-Z]+)@.mail.((([0-9a-zA-Z]+)|(''))\.)+((com)|(ru))'
    print (re.match(pattern, mail))

CheckValidMail('vova289@gmail.som.dom.com')
