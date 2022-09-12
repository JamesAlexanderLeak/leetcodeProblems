class Solution {
    public boolean isAnagram(String s, String t) {
        /*
        Given two strings s and t, return true if t is an anagram of s,
        and false otherwise.

        An Anagram is a word or phrase formed by rearranging the 
        letters of a different word or phrase,
        typically using all the original letters exactly once.        
        */
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) alphabet[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) alphabet[t.charAt(i) -'a']--;
        for (int i : alphabet) if (i != 0) return false;
        return true;
    }
}