import codecs
import argparse
import os.path
import re
import string
import collections


def load_data(filepath):
    with codecs.open(filepath, "r", "utf-8") as source_file:
        file_content = source_file.read()
        source_file.close()
        return file_content


def get_most_frequent_words(text):
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~–"""
    replace_punctuation = str.maketrans(' ', ' ', punctuation)
    text = text.lower().translate(replace_punctuation)
    counts = {}
    words = text.split()
    counter = collections.Counter(words)
    return counter.most_common()[:10]


def get_file_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file_path",
                        help="custom text file path")
    args = parser.parse_args()
    file_path = args.file_path
    if file_path is None:
        file_path = "text.txt"
    return file_path


if __name__ == '__main__':
    file_path = get_file_path()
    if not os.path.isfile(file_path):
        print("error: can't find file {}".format(file_path))
        sys.exit()
    text = load_data(file_path)
    most_frequent = get_most_frequent_words(text)
    for word in most_frequent:
        print(word[0])
