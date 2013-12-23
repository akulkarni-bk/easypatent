import os
import sys

class reader:
    def __init__(self, dir_to_read, dir_to_write):
        self.inp_dir = dir_to_read
        self.out_dir = dir_to_write

    def list_input_directory(self):
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

    def read_file(self, input_file):
        """
        Read file and chunk it into multiple patent claims.
        Write each individual patent to its own file.
        """
        fp = open(input_file, 'r')
        exp = re.compile("")
        if not fp:
            for line in fp:

        pass

    def write_file(self, out_file_name, out_file_data):
        """
        Write the file with given name and given data.
        """
        pass

    def iterate_on_dirs(self):
        """
        Iterate on the list of input files and write out respective patent files with its content.
        """
        pass


