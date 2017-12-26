from urllib.request import urlopen
from html.parser import HTMLParser
from linkfinder import *
from general import *
from queue import Queue
from p_finder import *
import urllib.request
import urllib.parse
import re

cnt=1

class Spider:
    base_url = ''
    domain_name =''

    def __init__(self, base_url, domain_name,ready_queue,not_ready_queue):
        self.base_url = base_url
        self.domain_name = domain_name
        while True:
            if ready_queue.empty() == False:
                self.gather_links(ready_queue.get(False), ready_queue,not_ready_queue)


    def gather_links(self,page_url, ready_queue,not_ready_queue):
        html_string = ''
        response = ''
        html_bytes = ''

        try:
            response = urlopen(page_url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            finder = Linkfinder(self.base_url, page_url)
            finder.feed(html_string)

            while(finder.links.empty()==False):
                not_ready_queue.put(finder.links.get(False))

            values = {'s':'basics', 'submit':'search'}
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            req = urllib.request.Request(page_url, data)
            resp = urllib.request.urlopen(req)
            resdata = resp.read().decode('utf-8')
            parag = re.findall(r'<p>(.*?)</p>', resdata)
            st= re.findall(r'<title>(.*?)</title>', resdata)
            paragraph = ""
            title=st[0]
            for pp in parag:
                paragraph+=re.sub('<.*?>', "", pp)

            t = threading.Thread(target = Spider.write_data, args=(page_url, paragraph, title, cnt),)
            global cnt
            cnt = cnt+1
            t.start()
        except Exception as e:
            print(e)

    def write_data(link,text,title,cnt):
        name=str(cnt)+".txt"
        name="folder1/"+name
        f = open(name,'w')
        out=str(link)+"\n"+str(title)+"\n"+str(text)
        f.write(out)
        return
