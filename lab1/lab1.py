import os.path
import argparse
import sys


class LogParser:

    @staticmethod
    def parse_log(input_file, string_to_find):
        out = []
        with open(input_file) as file:
            data = file.read()
            file.close()
        splitted = data.split( "\n" )
        for word in splitted:
            if string_to_find in word:
                out.append(word)
        return out

    @staticmethod
    def get_parsed():
        parser = argparse.ArgumentParser()
        parser.add_argument("File")
        arg = parser.parse_args()
        return arg.File

    @staticmethod
    def save(file, out):
        with open(file, "w") as out_file:
            for line in out:
                out_file.write(line)
                out_file.write("\n")
            out_file.close()

class InputFileValidator():
    @staticmethod
    def validate(file_name):
        if os.path.isfile(file_name):
            return True
        else:
            sys.exit("file doesn't exist")


if __name__ == '__main__':
    File = LogParser.get_parsed()
    if InputFileValidator.validate(File):
        parsed = LogParser.parse_log(File, "PrChecker.Downs")
        LogParser.save("out.txt", parsed)
        os.system("jupyter notebook ./out_jupyter.txt")





