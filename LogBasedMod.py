import sys
import datetime
import operator
sys.path.append("../")
import SampleMod
import configparser

class LogBasedMod(SampleMod):
    __run():
        # reading the config
        config = configparser.ConfigParser()
        config.read('settings.ini')

        # reading the log
        directory = './data'
        for filename in os.listdir(directory):
            if filename.endswith(".log"):
                fh = open(os.path.join(directory, filename))
                self.input_from_file(fh)

        # parsing the log here

    __run = run
