class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t
        is an anagram of s, and false otherwise.
        """
        #check if lens are same, if not return false
        if len(s) != len(t):
            return False
        #check if both have same set, if not return false
        if set(s) != set(t):
            return False
        hashSTable = dict()
        hashTTable = dict()
        #count letters in s and store in dict
        for letter in s:
            hashSTable[letter] = hashSTable.get(letter,0) + 1
        #count letters in t and store in dict
        for letterT in t:
            hashTTable[letterT] = hashTTable.get(letterT,0) + 1
        #return bool of dictionaries equivalency
        return hashTTable == hashSTable