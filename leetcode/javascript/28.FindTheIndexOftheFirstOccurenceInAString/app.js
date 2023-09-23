/*
28. Find the Index of the First Occurence in a String

Given two strings needle and haystack, return the index of the first occurence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
*/

/*
BRUTE FORCE APPROACH
Time Complexity: O(MN) M being haystack length, N being length of needle
Space Complexity: O(N) N being dependent on length of needle

*/
var strStr = function(haystack, needle) {
    const firstLetter = needle[0]
    let p1 = 0
    let p2 = 0

    while (p2 < haystack.length) {
       if (firstLetter === haystack[p1]) {
        let res = ""
        let index = p1
        while (p2 < needle.length + p1) {
            res += haystack[p2]
            p2 ++
        }
        if (res === needle) return index
        else {
            p2 = p1
        }
       }
       p1 ++
       p2 ++
    }
    return -1 
}

// console.log(strStr("sadbutsad", "sad"))
// console.log(strStr("leetcode", "leeto"))
console.log(strStr("mississippi", "issip"))

