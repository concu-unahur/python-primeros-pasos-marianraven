import threading
import time
import logging
from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir():
    time.sleep(1)

def dormir2(seg)
    time.sleep(seg)
    
dormir2(1)
    
contador = Contador()
contador.iniciar()

for i in range(10):
    thread = threading.Thread(target=dormir)
    thread.start()

hilos = []

for i in range(10):
    thread = threading.Thread(target=dormir2, args=[1])
    hilos.append(thread)
    thread.start()
    thread.join()


    
contador.finalizar()
contador.imprimir()