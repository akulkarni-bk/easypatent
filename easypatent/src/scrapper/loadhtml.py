import urllib2
import os
import sys

class HTMLLoader:
    def __init__(self, html_link="http://www.google.com/googlebooks/uspto-patents-grants-text.html"):
        self.uri = html_link
        self.read_url()

    def read_url(self):
        response = urllib2.urlopen(self.uri)
        self.html = response.read()

    def get_html(self):
        return self.html

def print_usage():
    print "Usage: python loadhtml.py <url-to-the-html>"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
    else:
        loader = HTMLLoader(sys.argv[1])
        print loader.get_html()
