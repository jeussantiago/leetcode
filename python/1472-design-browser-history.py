class BrowserHistory:
    '''
    Stacks:
    [a,b,c,d,e]
    []

    __init__:
    T: O(1)
    S: O(1)

    visit:
    T: O(1) where s is the number of steps
    S: O(n) how many times visit is called

    back:
    T: O(s) where s is the number of steps
    S: O(n)

    forward:
    T: O(s) where s is the number of steps
    S: O(n)
    '''

    def __init__(self, homepage: str):
        # stacks
        self.history = [homepage]
        self.forw_history = []

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forw_history = []

    def back(self, steps: int) -> str:
        # you cant continuously go back to the previous url, there is an end which is the first url
        while len(self.history) > 1 and steps > 0:
            current_url = self.history.pop()
            self.forw_history.append(current_url)
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while self.forw_history and steps > 0:
            current_url = self.forw_history.pop()
            self.history.append(current_url)
            steps -= 1
        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
