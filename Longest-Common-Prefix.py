class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return string
            string += char

        return string


        