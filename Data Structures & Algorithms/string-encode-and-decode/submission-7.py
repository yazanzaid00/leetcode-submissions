class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append((f'{len(string)}#{string}'))
        print("".join(res))
        return "".join(res) # how does join work?
    def decode(self, s: str) -> List[str]:
        #parse the length
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            curr_len = int(s[i:j])
            res.append(s[j + 1: j + curr_len + 1])
            i = j + curr_len + 1
        return res