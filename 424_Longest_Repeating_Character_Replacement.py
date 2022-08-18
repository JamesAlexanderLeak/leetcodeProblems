class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s and an integer k. You can
        choose any character of the string and change it to
        any other uppercase English character. You can perform
        this operation at most k times.

        Return the length of the longest substring containing the
        same letter youc an get after performing the above operations.

        Example:
        Input: s = "ABAB", k=2
        Output: 4
        since A or B can be replaced
        """
        #create count dictionary to keep track of count of characters
        count = dict()
        #max frequency of character within window
        maxf = 0
        #result length
        res = 0
        #left pointer
        l = 0
        #right pointer
        for r in range(len(s)):
            #count character from right pointer
            count[s[r]] = 1 + count.get(s[r],0)
            #max characters that can be replaced
            maxf = max(maxf,count[s[r]])
            #while window length minus maxFrequency character is greater than k,
            #subtract character frequency from left by 1 and move left pointer forward
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+=1
            #set result to max between current window len and max window length
            res = max(res,r-l+1)
        #return result
        return res