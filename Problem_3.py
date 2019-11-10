#Using a list to represent sliding window
#Sliding window is the current unrepeated substring. Moving it though string s.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr=[]
        longest=0
        for x in s:
            if x in substr:
                start = substr.index(x)+1
                if start<len(substr):
                    substr=substr[start:]
                else:
                    substr=[]
                substr.append (x)
                if len(substr)>longest:
                    longest=len(substr)
            else:
                substr.append(x)
                if len(substr)>longest:
                    longest=len(substr)
    return longest
