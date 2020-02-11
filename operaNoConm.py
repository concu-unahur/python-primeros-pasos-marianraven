import threading
from threading import Lock
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
lock= threading.Lock()
numero=0

semaphoro= threading.Semaphore(3)
semaphoro.acquire()
logging.info(f'estamos corriendo semaforo 1')
semaphoro.acquire()
logging.info(f'estamos corriendo semaforo 2')

def agregarUno():
    global numero
    global semaphoro
    semaphoro.acquire()
    try:
         numero+=1
         logging.info(f'numero ={numero}')
         logging.info(f'suma')
    finally:
         logging.info(f' ahora numero es igual a = {numero}')
         semaphoro.release()
   


def agregarTres():
     global numero
     global lock
     lock.acquire()
     try:
        numero+=3
        logging.info(f'numero ={numero}')
        logging.info(f'suma de a tres')
     finally:
        logging.info(f' ahora numero es igual a = {numero}')
        lock.release()


def multiplicarDos():
    global numero
    global lock
    lock.acquire()
    try:
        numero*=2
        logging.info(f'numero ={numero}')
        logging.info('multiplicar')
    finally:
        logging.info(f'ahora numero es igual a = {numero}')
        lock.release()


t1 = threading.Thread(target=agregarUno)
t2 = threading.Thread(target=agregarTres)
t3 = threading.Thread(target= multiplicarDos)


t3.start()
t1.start()
t2.start()



logging.info({numero})




