class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = "".join([c for c in s if c in alphanumeric])
        return s == s[::-1]
        