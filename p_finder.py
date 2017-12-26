import threading
from html.parser import HTMLParser
from urllib.request import urljoin
import file_manager
import os
import pickle
import os.path



class P_finder(HTMLParser):

    def __init__ (self , base_url , page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.ptag=""
        self.ttag=""
        self.title=""
        self.found = True
        self.para = page_url + '\n'

    def handle_starttag(self , tag , attrs):

        if tag == 'p' :
            self.ptag=tag
        if tag == 'title':
            self.ttag=tag
    def handle_data(self, data):
        if self.ttag=='title' and self.found == True:
            self.found = False
            self.title = data
            para += self.title + '\n'
            return

    def handle_data(self, data):
        if self.ptag=='p':
            self.para += data

    def page_links(self):
        return self.para


    def error(self, message):
        pass
