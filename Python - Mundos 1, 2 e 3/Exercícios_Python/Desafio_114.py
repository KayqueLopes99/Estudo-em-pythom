# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
#  Biblioeca de acesso ao site
import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen(  'https://www.youtube.com/watch?v=NxOjB7gjack')
except urllib.error.URLError:
    print('\033[91mERRO - O site não está acessível -\033[m')
else:
    print("\033[92mSUCESSO - O site está acessível - \033[m")
    # Codigo do site. print(site.read())
