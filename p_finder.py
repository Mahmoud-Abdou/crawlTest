import threading
from html.parser import HTMLParser
from urllib.request import urljoin
import file_manager
import os
import pickle
import os.path
cnt=1

class P_finder(HTMLParser):

    def __init__ (self , base_url , page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.ptag=""
        self.ttag=""
        self.title=""

    def handle_starttag(self , tag , attrs):
        if tag == 'p' :
            self.ptag=tag
        if tag == 'title':
            self.ttag=tag

    def handle_data(self, data):
        para=""
        if self.ttag=='title':
            self.ttag=""
            self.title = data

        if self.ptag=='p':
            self.ptag=""
            para += data
            para+='\n'
            print("pparaaaaaaaa ya gama3a paraaa")
            t = threading.Thread(target = write_data,args=(self.page_url, para,self.title,cnt),)
            cnt=cnt+1
            t.start()

    def error(self, message):
        pass

def write_data(link,text,title,cnt):
    print ("cnt = "+cnt)
    name=str(cnt)+".txt"
    f = open(name,'w')
    out=str(link)+"\n"+str(title)+"\n"+str(text)
    f.write(out)
    return
