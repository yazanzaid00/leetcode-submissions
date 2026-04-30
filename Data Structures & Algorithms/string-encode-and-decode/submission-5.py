class Solution:
    lengths = []
    def encode(self, strs: List[str]) -> str:
        self.lengths.clear()
        my_str = ""
        
        for string in strs:
            self.lengths.append(len(string))
            my_str += string

        return my_str

    def decode(self, s: str) -> List[str]:
        result = []
        offset = 0
        for length in self.lengths:
            result.append(s[offset:length + offset])
            offset += length
        return result