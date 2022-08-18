class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest
        substring without repeating characters.
        """
        #current set of characters in substring
        chars = set()
        #left is left of substring
        left = 0
        #length is right-left + 1
        length = 0
        #move right forward
        for r in range(len(s)):
            #if right character is in chars, move left
            while s[r] in chars:
                #remove s[left] value from set
                chars.remove(s[left])
                #move left forward
                left = left+1
            #then add right value to set
            chars.add(s[r])
            #set maxLen to max between (right - left +1) and current length
            length = max(length,r-left+1)
        #return max length
        return length