class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maintain a sliding window
        # count how many elements there are
        # track how many of the most numerous elements there are
        # set / hashmap?

        l, r = 0, 0
        char_count = [0] * 26
        ans = 0
        while l <= r and r < len(s):
            # look at the new character
            c = s[r]

            char_count[ord(c) - ord("A")] += 1
            # Current K will be

            to_replace = r - l + 1 - max(char_count)


            # if we exceed number              
            while to_replace > k:
                print(char_count)
                to_remove = s[l]
                char_count[ord(to_remove) - ord("A")] -= 1
                l += 1
                to_replace = l - r + 1 - max(char_count)
            

            ans = max(ans, r - l + 1)
            r += 1
        
        return ans

                