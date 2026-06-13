class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_count = [0] * 26
        ans = 0
        maxf = 0
        while l <= r and r < len(s):
            c = s[r]
            char_count[ord(c) - ord("A")] += 1

            maxf = max(maxf, char_count[ord(c) - ord("A")])
            # Banking on the fact that this is O(1) because the list is constant in size
            to_replace = r - l + 1 - maxf
            
            while to_replace > k:
                to_remove = s[l]
                char_count[ord(to_remove) - ord("A")] -= 1
                l += 1
                to_replace = l - r + 1 - maxf
            

            ans = max(ans, r - l + 1)
            r += 1
        
        return ans

                