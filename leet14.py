class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix

strs =
["flower","flow","flight"]
Output
"fl"
Expected
"fl"
