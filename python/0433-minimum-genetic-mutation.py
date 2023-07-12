class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        - convert bank to a set

        - at each position in the curretn gene, change it to one of the four possible characters "ACGT"
        - this makes sure that theres only a one mutation difference
        - if this new mutation is in the endGene,
            - add to queue
            - remove from endGene

        - if the node == endGene, then return the number of steps

        m is the length of gene
        n is the length of bank
        Time: O(nm)
            ; (n) convert list bank into set bank
            (n * m)
            ; (m) change one letter at a time
            ;   (1) check if new mutation is in the bank
            ; (n) this checking operation to go from startGene to endGene can only realistically continue
            ; for however many letters there are since you would just change one letter but that would
            ; bring us to every item in bank
            ; (n*m + n) => (n*m)
        Space: O(n)
            ; set bank
        '''
        bank = set(bank)
        q = collections.deque([startGene])
        steps = 0
        while q:
            for _ in range(len(q)):
                gene = q.pop()
                if gene == endGene:
                    return steps

                for c in "ACGT":
                    for i in range(len(gene)):
                        mutation = gene[:i] + c + gene[i + 1:]
                        if mutation in bank:
                            q.appendleft(mutation)
                            bank.remove(mutation)

            steps += 1

        return -1

        '''
        "AACCTTGG"
        "AATTCCGG"
        ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
        => -1

        - you need to jump from one mutation to another
        - one mutation is defined by a single letter difference
        - those are the only jumps you can make
        - if there is more than that, then you can't make that mutation unless you visit
        some other mutation and that mutation is 1 mutation away from the target

        - so this is a graph problem
        
        - traverse through each string, compare it with the other, 
            - if they are 1 mutation away, then add each other to each others adj list

        if the endGene is not in the bank,
            - then its impossible to get to the endgene
            - return -1
        - add the startGene in the bank
        ["AACCGGTT","AACCGGTA","AACCGCTA","AAACGGTA"]
        - will be using the index
        {
            0: [1]
            1: [0,2,3]
            2: [1]
            3: [1]
        }

        Traverse the graph starting at the startGene, in this scenario, start at position 0
        - stop the graph is bank[current_ind] == endGene

        n is the length of bank
        e is the number of edges/one mutation
        Time: O()
            ; n^2 create the adj list
            ; (e + n) traverse the adj list
        Space: O(n^2)
        '''
