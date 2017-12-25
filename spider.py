from urllib.request import urlopen
from html.parser import HTMLParser
from linkfinder import *
from general import *
from queue import Queue
from p_finder import *

cnt=1

class Spider:
    base_url = ''
    domain_name =''

    def __init__(self, base_url, domain_name,ready_queue,not_ready_queue):
        self.base_url = base_url
        self.domain_name = domain_name
        while True:
            if ready_queue.empty() == False:
                #print(ready_queue.get(False))
                self.gather_links(self.base_url, ready_queue,not_ready_queue)


    def gather_links(self,page_url, ready_queue,not_ready_queue):
        html_string = ''
        response = ''
        html_bytes = ''

        try:
            response = urlopen(page_url)
            #if response.getheader('content-Type') == 'text/html' :
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            finder = Linkfinder(self.base_url, page_url)
            finder.feed(html_string)
            while(finder.links.empty()==False):
                not_ready_queue.put(finder.links.get(False))
            pfinder = P_finder(self.base_url, page_url)
            pfinder.feed(html_string)
            #print(pfinder.para)
            #print('------------------------------------------------------------------------------------------------------------------------')
            #t = threading.Thread(target = write_data,args=(page_url, pfinder.para,self.title,cnt),)
            global cnt
            cnt = cnt+1
        #    t.start()
        except Exception as e:
            print(e)

    def write_data(link,text,title,cnt):
         name=str(cnt)+".txt"
         f = open(name,'w')
         out=str(link)+"\n"+str(title)+"\n"+str(text)
         f.write(out)
         return
