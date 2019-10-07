import re

def CheckValidURL(url):
    pattern = '(http|https)://([0-9a-zA-Z]+)\.(.+)(((/[0-9a-zA-Z]+)|('')))+'
    print (re.match(pattern, url))

CheckValidURL('https://proglib.io/p/ds-in-3months/')
