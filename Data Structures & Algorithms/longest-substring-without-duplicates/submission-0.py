class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a sliding window containing a set of elements
        # if there is a a dupe found by r, then we shift l until
        # we reach a state of non dupes, meaning we shift it until
        # the dupe
        if len(s) == 0:
            return 0

        track = {}
        best = 0
        count = 0
        l, r = 0, 0
        while l <= r and r < len(s):
            print(track)
            print(l, r)
            new_char = s[r]
            if new_char in track:
                # dupe found we advance till we drop it
                track[new_char] = r
                while True:
                    if s[l] == new_char:
                        # we found it
                        print("hi")
                        l += 1
                        break
                    else:
                        # we didn't find it yet
                        print(track)
                        print(s[l])
                        del track[s[l]]
                        l += 1
                        count -= 1
                        continue
                r += 1
            else:
                track[new_char] = r
                r += 1
                count += 1
                best = max(count, best)
        return best
