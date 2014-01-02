from HTMLParser import HTMLParser
from loadhtml import HTMLLoader
import re
class Scraper:
    def __init__(self):
        loader = HTMLLoader()
        self.html = loader.get_html()
        self.parser = Parser()

    def scrape(self):
        link = self.parser.feed(self.html)

    def getZipLinks(self):
        return self.parser.getZipLinks()

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link_dict = dict()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if len(attr) > 1:
                    if attr[0] == "href":
                        if self.isUrlUseful(attr[1]):
                            #print attr[1]
                            if attr[1] not in self.link_dict:
                                self.link_dict[attr[1]] = 1
                            else:
                                self.link_dict[attr[1]] = self.link_dict[attr[1]] + 1
                        else:
                            continue
    
    def isUrlUseful(self, url):
        regex = re.compile("^http://storage.googleapis.com/(.*)\.zip$")
        m = regex.match(url)
        if m != None:
            return True
        else:
            return False

    def getZipLinks(self):
        return self.link_dict

if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape()

