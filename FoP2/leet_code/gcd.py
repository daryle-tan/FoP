class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        min_len = min(len(str1), len(str2))

        for i in range(min_len, 0, -1):
            prefix = str1[:i]

            if len(str1) % len(prefix) == 0 and len(str2) % len(prefix) == 0:
                if prefix * (len(str1) // len(prefix)) == str1 and prefix * (len(str2) // len(prefix)) == str2:
                    return prefix

        return ""
            