class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(f"{len(string)}#{string}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while r < len(s) and s[r] != "#":
                r += 1
            length = int(s[l:r])
            res.append(s[r+1:r+1+length])
            r += length + 1
            l = r
        return res