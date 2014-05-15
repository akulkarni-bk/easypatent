import os
import sys
from lxml import etree
import gzip

class reader:
    def __init__(self, dir_to_read, dir_to_write):
        self.inp_dir = dir_to_read
        self.out_dir = dir_to_write
        self.load_input_directory()

    def load_input_directory(self):
        """
        Create a list of files in the input directory
        Store them in the object variable.
        """
        if os.path.exists(self.inp_dir) and os.path.exists(self.out_dir):
            self.files_list = os.listdir(self.inp_dir)
            if len(self.files_list) < 1:
                print "No files found in the input directory: %s"%(self.inp_dir)
            else:
                print "%d files found in the input directory."%(len(self.files_list))
        else:
            print "Input or Output directory not found."
            return -1

    def read_zip_write_xmls(self, input_file):
        """
        Read file and chunk it into multiple patent claims.
        Write each individual patent to its own file.
        """
        filepath = os.path.join(self.inp_dir, input_file)
        fp = gzip.open(filepath, 'rb')
        lines = []
        if fp:
            ziplines = fp.read()
            for line in ziplines:
                if line.startswith("<?xml "):
                    [docID, title] = self.parse_xml(''.join(lines))
                    file_name = docID + ".xml"
                    self.write_file(file_name, ''.join(lines))
                    lines = []
                    lines.append(line)
                    file_name =""
                else:
                    lines.append(line)
        fp.close()

    def _first(self, array, default = None):
        for item in array:
            return item
        return default

    def parse_xml(self, buff):
        doc = etree.XML(buff)
        docID = "-".join(doc.xpath('//publication-reference/document-id/*/text()'))
        title = self._first(doc.xpath('//invention-title/text()'))
        return [doctID, title]

    def write_file(self, out_file_name, out_file_data):
        """
        Write the file with given name and given data.
        """
        filepath = os.path.join(self.out_dir, out_file_name)
        fp = open(filepath, 'w')
        if fp:
            fp.writelines(out_file_data)
        else:
            print "Sorry could not open file %s for writing."%(filepath)

    def iterate_on_dirs(self):
        """
        Iterate on the list of input files and write out respective patent files with its content.
        """
        for f in self.files_list:
            print "processing file %s."%(f)
            self.read_zip_write_xmls(f)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        rdr = reader(sys.argv[1], sys.argv[2])
        rdr.iterate_on_dirs()
    else:
        print "Command came in with : " + sys.argv
