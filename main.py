
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import os 

try:

    documetos = os.listdir('/home/alemao/Documentos/PYTHON/novo-projeto')
    print('--> PASTA DOCUMENTOS <--')

    for i in documetos:
        print(f'{i}\n')

    resp = str(input('Qual o nome do arquivo que desenha salvar: ')).strip()

    arq = open(f'{resp}.txt', 'a')
    
    url = str(input('URL: ')).strip()
    while True:
        resp = str(input('''
        [1] - HMTL
        [2] - HEAD
        [3] - BODY
        [4] - H1
        [5] - exit
        
        Qual tag HMTL deseja capturar?
        > ''')).strip()[0]
        
        if resp == '1':
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            print(bs.html)
            doc = str(bs.html)
            arq.write(doc)      

        elif resp == '2':
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            print(bs.head)
            doc = str(bs.head)
            arq.write(doc)      

        elif resp == '3':
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            print(bs.body)
            doc = str(bs.body)
            arq.write(doc)      

        elif resp == '4':
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            print(bs.h1)
            doc = str(bs.h1)
            arq.write(doc)      


        elif resp == '5':
            break
            

        else:
            print('COMMAND NOT RECOGNIZED TRY AGAIN!')
            pass
            arq.close()

except HTTPError as e:
    print(e)

except URLError as e:
    print(e)

except KeyboardInterrupt as e:
    print(e)

