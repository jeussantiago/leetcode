class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        - choose a symbol that isnt ascii unichar char
        """
        if len(strs) == 0:
            return chr(257)

        return chr(258).join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        if s == chr(257):
            return ""

        return s.split(chr(258))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
