from urllib.request import urlopen
from html.parser import HTMLParser
from linkfinder import *
from general import *
from queue import Queue
from p_finder import *
class Spider:
    base_url = ''
    domain_name =''

    def __init__(self, base_url, domain_name,ready_queue,not_ready_queue):
        self.base_url = base_url
        self.domain_name = domain_name
        while True:
            if ready_queue.empty() == False:
                print(ready_queue.get(False))
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
        except Exception as e:
            print(e)

