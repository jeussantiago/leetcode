class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # s = "wordgoodgoodgoodbestword"
        # words = ["word","good","best","good"] # output = [] expectecd = [8]
        # s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        # words = ["fooo","barr","wing","ding","wing"] # output = [], expected = [13]
        '''
        - approach is to create a temporary list which holds the same elements as the normal list
        - remove an element from that copied list if the word is presnt
        - if the list is empty than save the start of the substring to results
        Time: O(n*m*k) where n is the size of the string (s) and m is the size of words being copied into the list, and
        k is the length of the substring checking for words

        '''
        res = []
        # concatenated substring has to be of this length
        one_word_size = len(words[0])
        subSize = len(words) * one_word_size
        for i in range(0, len(s) - subSize + 1):
            temp_words = words.copy()
            curr_word = s[i:i+one_word_size]
            if curr_word in temp_words:
                step = 0
                while len(temp_words) != 0:
                    curr_word = s[i+step:i+one_word_size+step]
                    if curr_word not in temp_words:
                        break
                    temp_words.remove(curr_word)
                    step += one_word_size
                if len(temp_words) == 0:
                    res.append(i)
        return res

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        Check all indices using hash table with count
        - create a hash table with the number of times a word appears in the list (since items in list can duplicate)
        - iterate through all the characters in a words
        - check the word, since its all the same length, to see if its in a hash table
        - if it is, reduce the count in the hash table
        - otherwise break out of loop/stop check substring
        - keep track of the number of words used to know if theres something left unused
        - if number of words used == len(words list), we know we have the index
        Space: O(a+b) where a is the number of unique elements in words and b is the substring
        '''
        res = []
        one_word_size = len(words[0])
        words_list_size = len(words)
        s_size = len(s)
        substring_size = one_word_size * words_list_size
        word_count = collections.Counter(words)

        def check(i):
            curr_word_count = word_count.copy()
            words_used = 0

            for k in range(i, i+substring_size, one_word_size):
                curr_word = s[k:k+one_word_size]
                #searching for greater than 0 because a word that doesn't exist is going to be 0
                if curr_word_count[curr_word] > 0:
                    curr_word_count[curr_word] -= 1
                    words_used += 1
                else:
                    break
            return words_used == words_list_size

        for i in range(s_size - substring_size + 1):
            if check(i):
                res.append(i)
        return res




























                
