import codecs
import argparse
import os.path
import re
import string
import collections


def load_data(filepath):
    with codecs.open(filepath, "r", "utf-8") as source_file:
        file_content = source_file.read()
        return file_content


def get_most_frequent_words(text, word_count):
    punctuation_with_ndash = "{}-".format(string.punctuation)
    replace_punctuation = str.maketrans(" ", " ", punctuation_with_ndash)
    text = text.lower().translate(replace_punctuation)
    counts = {}
    words = text.split()
    counter = collections.Counter(words)
    most_common_words = counter.most_common(word_count)
    most_common_words_list = []
    for word, count in most_common_words:
        most_common_words_list.append(word)
    return most_common_words_list


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        dest="file_path",
        help="custom text file path",
        default="text.txt"
    )
    return parser.parse_args()


if __name__ == "__main__":
    file_path = get_args().file_path
    if not os.path.isfile(file_path):
        sys.exit("error: can't find file {}".format(file_path))
    text = load_data(file_path)
    word_count = 10
    most_frequent = get_most_frequent_words(text, word_count)
    print("most frequent words:")
    for word in most_frequent:
        print(word)
