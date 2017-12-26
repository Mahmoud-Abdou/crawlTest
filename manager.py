import file_manager
import queue
from threading import Thread
from domain import*
def check(link,ready_queue,mapp):
    head = link.split('/')[2]
    fm=file_manager.file_manager()
    vis=mapp.get(link,0)
    if(vis==0):
        mapp[link]=1
        ready_queue.put(link)
    return

def waiting(ready_queue,not_ready_queue,mapp):
    print("a7na mangers w23dyyn fe al reciption")
    while(True):
        if(not_ready_queue.empty()==False):
            g=not_ready_queue.get(False)
            check(g,ready_queue,mapp)
