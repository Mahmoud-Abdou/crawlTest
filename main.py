import threading
from queue import Queue
from spider import *
from domain import *
from general import *
from manager import *

PAGES = ['https://stackoverflow.com', 'https://stackoverflow.com', 'https://stackoverflow.com', 'https://stackoverflow.com']
depth = 0
not_ready_queue = Queue()
ready_queue = Queue()
ready_queue.put('https://stackoverflow.com')

def create_spiders():
    for i in PAGES:
        DOMAIN_NAME = get_domain_name(i)
        t = threading.Thread(target = Spider,args=(i, DOMAIN_NAME,ready_queue,not_ready_queue),)
        t.start()
        tt=threading.Thread(target= waiting , args=(ready_queue,not_ready_queue),)
        tt.start()
        return



create_spiders()



























'''
#threading
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work,args=(),)
        t.daemon = True
        t.start()

#queue links
def work(ready_queue):
    while True:
        url = ready_queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        ready_queue.task_done()

def create_jobs():
    ready_queue.join()
    global depth
    depth += 1
    while depth <10 :
        crawl()

def crawl():
    #queued_links = file_to_set(QEUEU_FILE)
    if ready_queue.empty() == True:
        # print(str(len(ready_queue)) + ' links in th queue')
         create_jobs()

create_spiders()
crawl()
'''

