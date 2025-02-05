// Example 1:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.

// Example 2:
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.

// Example 3:
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

function lengthOfLongestSubtring(s) {
  // keep track of words in hashmap.
  const hash = {};
  let currLength = 0;
  let totalLength = 0;

  if (s.length === 1) {
    return 1;
  }

  for (let i = 0; i < s.length; i++) {
    const word = s[i];
    if (!hash[word]) {
      hash[word] = 1;
    } else {
      currLength = 0;
    }

    currLength++;

    if (currLength > totalLength) {
      totalLength = currLength;
    }
  }

  console.log(totalLength);
  return totalLength;
}

lengthOfLongestSubtring("abcabcbb");
lengthOfLongestSubtring("bbbbb");
lengthOfLongestSubtring("pwwkew");
lengthOfLongestSubtring(" ");
lengthOfLongestSubtring("au");
lengthOfLongestSubtring("abc");
lengthOfLongestSubtring("dvdf");
