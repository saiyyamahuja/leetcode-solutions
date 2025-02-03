    def lengthOfLongestSubstringSimpler(self, s):
        seen = {}
        left, right = 0, 0
        longest = 1
        while right < len(s):
            longest = max(longest, right - left + 1)
            seen[s[right]] = right
            right += 1
        return longest