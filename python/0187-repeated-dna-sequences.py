class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        - no overlapping substrings
        - keep sequences seen in a set
        - if the current sequence is in the set, it is a repeating sequence
        (checking a set for an item is O(1) time)
            - save sequence to a result set

        Time: O(n)
        Space: O(n)
        '''
        seen_sequences = set()
        repeating_sequences = set()

        for i in range(len(s)-9):
            sequence = s[i:i+10]
            if sequence in seen_sequences:
                repeating_sequences.add(sequence)
            else:
                seen_sequences.add(sequence)

        return list(repeating_sequences)
