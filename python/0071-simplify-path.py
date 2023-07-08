class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        - has to start with "/"
        - ".." removes the last path/ goes to last directory if it is not root
        - consecutive "/" can be ignored

        Stack:
        1) add a directory to the stack
        2) if the directory is "..": pop from the stack
        3) if directory is ".": then nothing happens

        Time: O(n) where n is the length of the path
        Space: O(n) where n is the length of the path
        '''

        directs = [direc for direc in path.split('/') if direc]
        canonical_path = []
        for part in directs:
            if part == "..":
                if canonical_path:
                    canonical_path.pop()
            elif part != ".":
                canonical_path.append(part)

        canonical_path = "/" + "/".join(canonical_path)
        return canonical_path