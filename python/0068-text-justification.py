class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        - divide empty spaces evenly between words
            - if uneven, left will take more spaces
        - last line
            - normal text w/ one space between words
            - fill rest of right space with empty space
        - there has to be atleast one space between each word

        - add each consecutive word until the maxWidth is reached
            - if the maxWidth is not reached, and theres no more words
            (means it is the last line and we should just fill the leftover space with empty spaces)

            - if the maxWidth is reached, put the word back into the list and space out the currently word configuration
                To Space the current configuration:
                - find the indexes of empty spaces
                - from left to right, add 1 space until the maxWidth is reached
        
        Time: O(2n) where n is the length of the words list
            : O(n)
        Space: O(n) where n is len(words)

        '''

        def formatLine(line):
            #counter for length of line
            L = sum(len(s) for s in line)
            available_spaces = maxWidth - L
            space_locations = max(1, len(line)-1) #number of words need to put spaces after

            for i in range(space_locations):
                #determine the right amount of spaces for current word 
                num_spaces_for_word = math.ceil(available_spaces / space_locations)
                available_spaces -= num_spaces_for_word
                space_locations -= 1
                #add spaces to word
                line[i] = line[i] + (" " * num_spaces_for_word )

            return line

        res = []
        L = 0 #length of line
        line = [] # current line
        indx = 0
        while indx < len(words):
            word = words[indx]
            if L + len(word) > maxWidth:
                #format line
                formattedLine = "".join(formatLine(line)) # format line to include more spaces
                res.append(formattedLine)
                #reset current line and word count
                line = []
                L = 0
            else:
                #line has space for the word to be added
                line.append(word)
                L += len(word) + 1 # +1 to account for space after word
                indx += 1

        #remove whitespace count from last word
        L -= 1
        #last row, format it by adding whitespace to the right
        for i in range(len(line)-1):
            line[i] += " "
        #L value already accounts for space after adding word to list
        line[-1] += " " * (maxWidth - L)
        res.append("".join(line))

        return res





















        