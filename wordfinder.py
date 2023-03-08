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
        
        self.words = self.create_word_list(path)
        
        print(f"{len(self.words)} words read")

    def create_word_list(self, path):
        """reads file and creates list of words"""
        file = open(path)
        word_list = []
        for line in file:
            line = line.rstrip("\n")
            word_list.append(line)
        return word_list


    
    def random(self):
        """returns random word from list"""
        return choice(self.words)


