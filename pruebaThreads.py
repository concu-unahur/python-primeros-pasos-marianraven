import requests
import time
import logging
import threading

from operaNoConm import agregarUno
from operaNoConm import agregarTres
from operaNoConm import multiplicarDos


agregarUno = threading.Thread(target=agregarUno)
agregarTres = threading.Thread(target=agregarTres)

threads = [agregarUno,agregarTres]

for i in threads:
    i.start() 
