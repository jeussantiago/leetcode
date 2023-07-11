class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        DFS:

        equations = [["a","b"],["b","c"]], values = [2.0,3.0]

        graph = {
            a: {
                b: 2
            }
            b: {
                a: 1/2,
                c: 3
            }
            c: {
                b: 1/3
            }
        }

        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

        ["a","c"]
        curr = 'a' ; target = 'c'
        - c is not in 'a' neighbors
            - so can't conclude solution
        - visit all neighbors of 'a' to try to get to 'c'
            - when you vist that neighbor, multiply the current output by the multiplication value
            - in this case, we are going to neighbor b which has a value of 2
            1 * 2 = 2 as the current product going into next recursion
        - curr = 'b' ; target = 'c
        - c is in the direct neighbor of b so we can just return the value there which is 3

        - have to keep track of the visited chars


        - if dividend or divisor not in the graph, output has to be -1
        - if dividend == divisor, output has to be 1
        - else: backtrack

        N is the number of equations
        M is the number of queries
        Time: O(M * N)
                    ; for each query, search the graph which can take up to N times
        Space: O(N)
                    ; (N) recursion stack
                    ; (N) graph -> N edges and 2N nodes
                    ; (N) visited set

        {
            'a': defaultdict(None, {
                'b': 2.0
            }), 
            'b': defaultdict(None, {
                'a': 0.5, 
                'c': 3.0
            }), 
            'c': defaultdict(None, {
                'b': 0.3333333333333333
            })
        }
        '''

        def dfs(node, target, product, visited):
            visited.add(node)
            ans = -1
            neighbors = graph[node]
            if target in neighbors:
                ans = product * neighbors[target]
            else:
                for neigh, val in neighbors.items():
                    if neigh in visited:
                        continue
                    ans = dfs(neigh, target, product * val, visited)
                    if ans != -1:
                        # found our way to the target
                        break

            visited.remove(node)
            return ans

        graph = collections.defaultdict(collections.defaultdict)
        for (dividend, divisor), val in zip(equations, values):
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1 / val

        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ans = -1
            elif dividend == divisor:
                ans = 1
            else:
                visited = set()
                ans = dfs(dividend, divisor, 1, visited)

            res.append(ans)

        return res
