from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> wf = WordFinder("words.txt")
    6 words read

    >>> wf.random() in ["cat", "dog", "porcupine", "walrus", "sloth", "panda",]
    True

    """

    def __init__(self, path):
        """Read file and report number of items read"""

        file = open(path)
        self.words = self.get_filtered_words(file)

        print(f"{len(self.words)} words read")

    # get_word_list is probably a better name because it returns the word_list
    # def create_word_list(self, file):
    #     """reads file and creates list of words"""

    #     word_list = []
    #     for line in file:
    #         line = line.rstrip() # without any argument will remove all whitespace
    #         word_list = self.append_word(line, word_list)
    #     return word_list

    def get_filtered_words(self, word_list):

        return [word.rstrip() for word in word_list]

    # def append_word(self, line, word_list):
    #     """Appends the word on the line from the file to the word_list"""

    #     word_list.append(line)
    #     return word_list

    def random(self):
        """returns random word from list

        >>> wf = WordFinder("words.txt")
        6 words read

        >>> wf.random() in ["cat", "dog", "porcupine", "walrus", "sloth", "panda",]
        True

        """
        return choice(self.words)


class RandomWordFinder(WordFinder):
    """Subclass of WordFinder that allows users to pass in word lists with
       blank lines and comment lines that begin with #.

       >>> rwf = RandomWordFinder("words2.txt")
       6 words read

       >>> rwf.random() in ["cat", "dog", "porcupine", "walrus", "sloth", "panda",]
       True

    """

    def get_filtered_words(self, word_list):
        return [
            word.rstrip()
            for word in super().get_filtered_words(word_list)
            if word != "" and not word.startswith("#")
        ]

    # def append_word(self, line, word_list):
    #     """ If the line is not an empty string or a comment,
    #         appends the word on the line from the file to the word_list"""

    #     if line != "" and not line.startswith("#"):
    #         word_list.append(line)
    #     return word_list