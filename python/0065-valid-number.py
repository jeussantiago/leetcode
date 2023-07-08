class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        - "-" and "+" can only be used once
        - "." can only be used once
        - no letters w/ exception to "e" or "E"
        - if theres an "e", there needs to be numbers before and after
        '''
        # s = "99e2.5"
        # s = ".e1" #false
        # s = "+." # false
        # s = '4e+'
        # s = 'e.7e5'

        hasDecimal = False # .
        hasNumbers = False

        #lowercase string
        s = s.lower()

        #split at e - there should only be 2 string after that
        s_ends = [s]
        if "e" in s:
            #ex: e.7e5
            if s.count("e") > 1:
                return False

            s_ends = list(filter(None, s.split('e')))
            if len(s_ends) != 2:
                return False
            #no decimals after e
            if "." in s_ends[1]:
                return False
        
        for strng in s_ends:
            hasNumbers = False
            for i, c in enumerate(strng):
                #first character has to be +/-/ or a number
                #if +/- show up after that first character thne its False
                if (i > 0 and c == "+") or (i > 0 and c == "-"):
                    return False
                #character is a letter
                if c.isalpha():
                    return False
                #used the only instance of decimal allowed for the current string
                if c == ".":
                    #second decimal, not allowed
                    if hasDecimal:
                        return False
                    else:
                        hasDecimal = True
                #make sure the string has atleast one number
                if c.isdigit():
                    hasNumbers = True
            #no numbers means non valid string
            if not hasNumbers:
                return False

        return True


