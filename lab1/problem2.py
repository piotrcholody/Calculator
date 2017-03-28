import argparse
import sys
import logging
import datetime
from collections import Counter
from os.path import isfile

logging.basicConfig(filename="logs.log", level = logging.INFO)
logging.info("\nWORD COUNTER")
logging.info(datetime.datetime.now())


class CountWords:
    def __init__(self):
        pass

    @staticmethod
    def get_parsed():
        parser = argparse.ArgumentParser()
        parser.add_argument("File")
        arg = parser.parse_args()
        return arg.File



    @staticmethod
    def count_words(file_object):
        c = Counter()
        w = Counter()
        logging.info("Counting")
        with open(file_object, "r") as file_to_count:
               for x in file_to_count:
                   c.update(x)
                   w.update(x.split())
        totall = sum(1 for line in open(file_object, "r"))
        totalw = sum(w.values())
        totalc = sum(c.values())
        with open('output.txt', 'w') as file:
            file.write("characters: %d\n" % totalc)
            file.write("words: %d\n" % totalw )
            file.write("lines: %d\n" % totall)
        logging.info("Done counting, saving to file")




class InputFileValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate(file_object):
        logging.info("Checking file: " + file_object)
        if not isfile(file_object):
            logging.error("Wrong argument")
            sys.exit("Enter correct path to the file as argument")
        logging.info("File is valid")

CountWords.count_words(CountWords.get_parsed())
