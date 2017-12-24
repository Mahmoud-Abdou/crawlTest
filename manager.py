import file_manager
import queue
from threading import Thread
from domain import*
def koko(link,ready_queue):
    head = link.split('/')[2]
    fm=file_manager.file_manager()
    vis=fm.read_visited(head,link)
    if(vis==0):
        thread=Thread( target=fm.write_visited  ,args=( head,link), )
        thread.start()
        ready_queue.put(link)
    return

def waiting(ready_queue,not_ready_queue):
    print("na fe el matb5 a3ed mstny ya fandm")
    while(True):
        if(not_ready_queue.empty()==False):
            g=not_ready_queue.get(False)
            koko(g,ready_queue)

