#Using the method of expanding from a cental position
#The postion could be a char in string or the middle position of two chars in string
#Expanding rule: if the char before a palindromic substring is the same with the char after it, it can be expanded.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        if s is None:
            return s
        elif len(s)==0:
            return ''
        else:
            for i in range(len(s)):
                length1=expand(s, i, i)
                length2=expand(s, i, i+1)
                if length1>=length2:
                    max_len=length1
                else:
                    max_len=length2
                
                if max_len>end-start+1:
                    start=i-(max_len-1)//2
                    end=i+max_len//2
        return s[start:end+1]
    
def expand(s,start1,end1):
    left=start1
    right=end1
    while left>=0 and right<len(s) and s[left]==s[right]:
        left=left-1
        right=right+1
    #"left" stops at the one before the correct left index
    #"right" stops at the one after the correct right index
    # For example, if the correct substring is "bab" from index 0 to 2.
    # Now the indexes stop at -1 and 3
    # Therefore, the length is right-left-1, which is 3
    return right-left-1





