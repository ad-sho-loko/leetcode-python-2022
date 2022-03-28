class Solution3:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        end = 0  # endはiそのものだから直接置き換え可能。
        longest = 0

        for i, ch in enumerate(s):
            if ch in used and used[ch] + 1 > start:
                start = used[ch] + 1
            else:
                used[ch] = i
                longest = max(longest, end - start + 1)

            used[ch] = i
            end += 1

        return longest
