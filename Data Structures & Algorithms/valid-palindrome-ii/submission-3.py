class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right, k):
            if k < 0:
                return False
            if left >= right:
                return True
            if s[left] == s[right]:
                return is_palindrome(left + 1, right - 1, k)
            else:
                return (is_palindrome(left + 1, right, k - 1) or
                        is_palindrome(left, right - 1, k - 1)) 

        return is_palindrome(0, len(s) - 1, 1)
