import sys
import datetime
import operator
# this needs to be updated perhaps
sys.path.append("../")
import SampleMod
import configparser

class LogBasedMod(SampleMod):
    """
    this module will produce load with patterns matching
    the observed distribution from the log provided 
    """
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
