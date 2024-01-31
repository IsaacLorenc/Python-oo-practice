"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, path):
        """reads dictionary and prints how many words read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """iterates over each line and removes whitespaces"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """returns a random word"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):

    def parse(self, dict_file):
        """Iterates over each line and checks if line is stripped and skips comments"""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]