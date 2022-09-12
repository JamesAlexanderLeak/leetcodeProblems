import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.

        You can return the answer in any order.
         */
        HashMap<Integer,Integer> prevMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            
            if (prevMap.containsKey(nums[i])) {
                return new int[] {prevMap.get(num),i};
            }
            prevMap.put(diff,i);
        }
        return new int[] {};
    }
}