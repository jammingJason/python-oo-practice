"""Word Finder: finds random words from a dictionary."""
from random import randint, random
from timeit import repeat


class WordFinder:
    def __init__(self, file_name):
        self.file_name = file_name
        self.new_file = []

    def get_words(self):
        file_contents = open(self.file_name)

        for line in file_contents:
            self.new_file.append(line.replace('\n', ''))

        file_contents.close()

    def random(self):
        self.get_words()
        list_length = len(self.new_file)
        return (self.new_file[randint(0, list_length-1)])


class RandomWordFinder(WordFinder):
    def __init__(self, file_name):
        super().__init__(file_name)

    def random(self):
        random_word = super().random()
        if random_word == '' or random_word.startswith('#'):

        else:
            return random_word
        # return super().random()
