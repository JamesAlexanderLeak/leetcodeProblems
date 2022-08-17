class Solution:
    def isPalindrome(self,s: str) -> bool:
        """
        A phrase is a palindrome if, after converting
        all uppercase letters into lowercase letters and
        removing all non-alphanumeric characters, it reads
        same forward and backward. Given a string s,
        return True if it is a palindrome, or false
        otherwise.
        """
        #two pointer so solution is O(n)
        left,right = 0,len(s)-1
        #while pointers don't cross
        while left < right:
            #search forward from front for alphanum chars
            while left < right and not s[left].isalnum():
                left+=1
            #search backward from end for alphanum chars
            while left < right and not s[right].isalnum():
                right-=1
            #if left and right are not equal, return false
            if s[right].lower() != s[left].lower():
                return False
            left+=1
            right-=1
        #return True if pointers cross
        return True