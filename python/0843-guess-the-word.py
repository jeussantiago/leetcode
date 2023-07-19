# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        '''
        - get the score of a random word
        - this means that the secret word if matched against the random_word
        should also get the same score value

        - compare current word with every other words in array
            - if the score comparison == Master score of the random_word
                - then this current word could possibly be the secret word

        secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"]

        random_word = "ccbazz"
        master_score = 3

        comparing random_word with other words:
        ccbazz vs acckzz -> score=3
        ccbazz vs eiowzz -> score=2
        ccbazz vs abcczz -> score=2

        - acckzz has the same score as the master_score (3) so we let it go to the next round

        worst case:
        words = ['aaaaaa','bbbbbb','cccccc','zzzzzz'] ; secret = 'zzzzzz'
            - could of randomed every word that is not simlar to secret at all
            - each iteration of words array gets reduced by -1 length each time

        n is th length of words
        Time: O(n^2)
            ; (1) choosing random word
            ; (1) get score from master
            ; (n * n) compare current word with rest of words

        Space: O(1)
            ; (1) we are recycling the given words arr, and it's only getting smaller(no extra space created)
        '''
        random_word_score = 0
        while random_word_score != 6:
            random_word = random.choice(words)
            random_word_score = master.guess(random_word)

            next_words_batch = []
            for word in words:
                if word != random:
                    if self.compareWords(random_word, random_word_score, word):
                        next_words_batch.append(word)

            words = next_words_batch

    def compareWords(self, word1, word1_score, word2):
        word2_score = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                word2_score += 1

        if word1_score == word2_score:
            return True
        return False
