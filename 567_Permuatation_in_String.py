class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains
        a permuation of s1, or false otherwise.

        In other words, return true if one of s1's permuations is the
        substring of s2.
        """
        #if s1 cannot fit into s2, return False
        if len(s2) < len(s1):
            return False
        #create alphabet for char count
        s1Count = [0] * 26
        s2Count = [0] * 26
        #find counts within first substring of s2 with len of s1
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        #find number of char matches between s1count and s2 count
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        #sliding window
        l = 0
        #start at end of s1 since we have already taken care of first range
        for right in range(len(s1),len(s2)):
            #if current window has all characters in alphabet matching, return True
            if matches == 26: return True
            #find character to add
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1
            #update matches
            #if s1Count[right letter] == s2Count[right letter], increase matches count
            if s1Count[index] == s2Count[index]:
                matches+=1
            #if previously a match but not anymore, decrement matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches-=1

            #set index to left pointer
            index = ord(s2[l]) - ord('a')
            #remove left from s2Count
            s2Count[index] -= 1
            #update matches
            #if s1Count[left letter] == s2Count[left letter], increase matches count
            if s1Count[index] == s2Count[index]:
                matches+= 1
            #if previously a match but not anymore, decrement matches
            elif s1Count[index] -1 == s2Count[index]:
                matches-= 1
            #move left pointer forward
            l+= 1
        #check if matches at end of loop.
        return matches == 26