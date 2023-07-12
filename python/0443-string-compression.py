class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        ["a","a","b","c","c","c"]
        result = [a, 2, b, c 3]
        ["a","a","b","c","c","a"]
        result = [a, 2, b, c, 2, a]

        - one pointer iterating entire array  (i)
        - another pointer to place the numbers (counter_index)
        - counter to show how many repeating chars (count)

        - if chars[counter_index] != chars[i]
            # insert the char
            - counter_index = chars[i-1] 
            counter_index += 1

            # add the count
            - add the number if counter is greater than 1
                - counter_index = count
                counter_index += 1

            count = 1

        - else
            count += 1

        Time: O(n)
        Space: O(1)
        '''

        chars.append(None)
        count = 1
        counter_index = 0

        for i in range(1, len(chars)):
            if chars[i] != chars[i-1]:
                chars[counter_index] = chars[i-1]
                counter_index += 1
                if count > 1:
                    for n in str(count):
                        chars[counter_index] = n
                        counter_index += 1

                count = 1
            else:
                count += 1

        return counter_index
