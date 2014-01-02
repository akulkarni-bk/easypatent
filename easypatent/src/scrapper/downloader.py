import urllib2
import os
import sys
from scraper import Scraper

class Downloader:
    def __init__(self, outdir):
        self.scrpr = Scraper()
        self.scrpr.scrape()
        self.size = 0
        self.outdir = outdir

    def getFileUrls(self):
        self.fileUrls = self.scrpr.getZipLinks()

    def getFileSize(self, url, urlobj):
        meta = urlobj.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        self.size += file_size

    def openUrl(self, url):
        urlobj = urllib2.urlopen(url)
        return urlobj

    def iterateThroughFiles(self):
        self.getFileUrls()
        for url in self.fileUrls:
            urlobj = self.openUrl(url)
            [dir, fileName] = self.getFileYearAndName(url)
            dirPath = self.mkDirectory(dir)
            self.getFileSize(url, urlobj)
            self.saveFile(fileName, dirPath, urlobj)
        print "Total file size is : %d"%(self.size)

    def getFileYearAndName(self, url):
        return [url.split('/')[-2], url.split('/')[-1]]

    def mkDirectory(self, dir):
        if not os.path.exists(os.path.join(self.outdir, dir) ):
            os.mkdir(os.path.join(self.outdir, dir))
        return os.path.join(self.outdir, dir)

    def saveFile(self, fileName, dirPath, urlobj):
        fp = open(os.path.join(dirPath, fileName), 'wb')
        block_size = 8192
        while True:
            buffer = urlobj.read(block_size)
            if not buffer:
                break
            fp.write(buffer)
        fp.close()
        print "Downloaded : %s"%(os.path.join(dirPath, fileName))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Error: Please provide output directory to store the files in."
    d = Downloader(sys.argv[1])
    d.iterateThroughFiles()


