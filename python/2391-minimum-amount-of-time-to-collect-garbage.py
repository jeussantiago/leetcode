class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        '''
        - we need to travaerse garbage to find out the last position for 
        metal(M), paper(P), and glass(G)


        - go through the garbage array again
        - at each position, convert the string into a hashmap with how many times
        the garbage appears (this is constant space since theres only 3 types)

        - check if the current house(ith) is <= the last position of the garbage

        Time: O(n)
            ; (n) find last position of garbage - iterating through array
            ; (n) findind the total time - iterating through array again
            ; (1) convert ith garbage into hashmap - but there is a max of 
            ; length 10 for the garbage[i] - constant time
        Space: O(1)
            ; (1) space usage for hashmap but there is a max of 
            ; length 10 for the garbage[i] - constant time

        Alternative is to 
        - find get the prefix sum of travel, 
        - get the prefix sum of garbage
        - find the last instances of metal(M), paper(P), and glass(G)
        - then just add the positions for those 3 into the results
        '''

        last_metal_pos = last_paper_pos = last_glass_pos = -1
        for i, gar in enumerate(garbage):
            gar_set = set(gar)

            if "M" in gar_set:
                last_metal_pos = i

            if "P" in gar_set:
                last_paper_pos = i

            if "G" in gar_set:
                last_glass_pos = i

        # modified array cause lazy to write more conditionals in loop
        travel = [0] + travel

        total_time = 0
        for i, gar in enumerate(garbage):
            gar_cnt = collections.Counter(gar)

            if i <= last_metal_pos:
                total_time += gar_cnt['M'] + travel[i]

            if i <= last_paper_pos:
                total_time += gar_cnt['P'] + travel[i]

            if i <= last_glass_pos:
                total_time += gar_cnt['G'] + travel[i]

        return total_time
