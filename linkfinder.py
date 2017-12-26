
from html.parser import HTMLParser
from urllib.request import urljoin
from queue import Queue
class Linkfinder(HTMLParser):

    def __init__ (self , base_url , page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links =Queue()

    def handle_starttag(self , tag , attrs):
        if tag == 'a' :
            for(attribute , value) in attrs:
                if attribute == 'href' :
                    url = urljoin(self.base_url , value)
                    full_link = url ;
                    self.links.put(full_link)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
