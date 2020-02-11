import threading
import time
import logging
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


semaphoro= threading.Semaphore(5)

semaphoro.acquire()
logging.info('quedan 4')

semaphoro.acquire()
logging.info('quedan 3')
semaphoro.acquire()
logging.info('quedan 2')
semaphoro.acquire()
logging.info('quedan 1')

semaphoro.release()
logging.info('no se ejecuta')