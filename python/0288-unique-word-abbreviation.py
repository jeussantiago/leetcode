class ValidWordAbbr:
    '''
    len(word) - 2

    - if the abbreviation doesn't exist in the original set
    - if the abbreaviation exist, the words have to be the same

    - there might be initialized words that have the same abbreviation so we need to remember all those words

    dictionary
    key=abbreviation
    val=list of words

    init:
    T: O(n) where n is the number of words in the dictionary
    S: O(n)

    isUnique:
    T: O(1)
    S: O(n)
    '''

    def __init__(self, dictionary: List[str]):

        self.words = collections.defaultdict(set)
        for word in dictionary:
            abbreviation = word
            if len(word) > 2:
                abbreviation = word[0] + str(len(word) - 2) + word[-1]

            self.words[abbreviation].add(word)

    def isUnique(self, word: str) -> bool:
        abbreviation = word
        if len(word) > 2:
            abbreviation = word[0] + str(len(word) - 2) + word[-1]

        if abbreviation not in self.words:
            return True
        else:
            words_with_abbreviation = self.words[abbreviation]
            if word in words_with_abbreviation and len(words_with_abbreviation) == 1:
                return True
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
