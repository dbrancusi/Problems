# A O(n ^ 2) time and O(1) space program to find the  
# longest palindromic substring 
  
# This function prints the longest palindrome substring (LPS) 
# of str[]. It also returns the length of the longest palindrome 
# def longestPalSubstr(string): 
#     maxLength = 1
  
#     start = 0
#     length = len(string) 
  
#     low = 0
#     high = 0
  
#     # One by one consider every character as center point of  
#     # even and length palindromes 
#     for i in xrange(1, length): 
#         # Find the longest even length palindrome with center 
#     # points as i-1 and i. 
#         low = i - 1
#         high = i 
#         while low >= 0 and high < length and string[low] == string[high]: 
#             if high - low + 1 > maxLength: 
#                 start = low 
#                 maxLength = high - low + 1
#             low -= 1
#             high += 1
  
#         # Find the longest odd length palindrome with center  
#         # point as i 
#         low = i - 1
#         high = i + 1
#         while low >= 0 and high < length and string[low] == string[high]: 
#             if high - low + 1 > maxLength: 
#                 start = low 
#                 maxLength = high - low + 1
#             low -= 1
#             high += 1
  
#     print "Longest palindrome substring is:", 
#     print string[start:start + maxLength] 
  
#     return maxLength 
  
# # Driver program to test above functions 
# string = "forgeeksskeegfor"
# print "Length is: " + str(longestPalSubstr(string)




class Solution(object):
    def longestPalindrome(self, s):
        largest = ''
        for i in range(len(s)):
            odd_palindrome = self.largestPalindroomeIndex(s, i, i)
            even_palindrome = self.largestPalindroomeIndex(s, i, i + 1)

            larger = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome

            largest = largest if len(larger) < len(largest) else larger

        return largest


    def largestPalindroomeIndex(self, string, left, right):
        leftIndex = 0
        rightIndex = 0

        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                leftIndex = left
                rightIndex = right
            else: 
                break

            left-=1
            right+=1

        return string[leftIndex:rightIndex+1]
















