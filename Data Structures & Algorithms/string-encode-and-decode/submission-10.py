class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for cur_str in strs:
            res.append(f"{len(cur_str)}#{cur_str}")

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while r< len(s) and s[r] != "#":
                r += 1
            str_len = int(s[l:r])
            res.append(s[r + 1: r + 1 + str_len])
            l = r + 1 + str_len
        return res