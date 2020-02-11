import requests
import time
import logging
import threading
from operaNoConm import agregarUno
from operaNoConm import agregarTres
from operaNoConm import multiplicarDos


agregarUno = threading.Thread(target=agregarUno)
agregarTres = threading.Thread(target=agregarTres)
multiplicarDos = threading.Thread(target=multiplicarDos)
threads = [agregarUno,agregarTres, multiplicarDos]

for i in threads:
    i.start() 