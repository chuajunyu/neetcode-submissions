class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def get_index(char: str):
            return ord(char) - ord("A") if ord(char) < ord("a") else ord(char) - ord("a") + 26

        tset = set(t)
        tcount = [0] * 52
        for x in t:
            tcount[get_index(x)] += 1

        l, r = 0, 0
        best = None
        have = 0
        while l <= r and r < len(s):
            c = s[r]
            
            if c in tset:
                # check if it fulfils criteria
                tcount[get_index(c)] -= 1

                if tcount[get_index(c)] == 0:
                    have += 1
                
                
                while have == len(tset):
                    while s[l] not in tset:
                        l += 1
                    if best is None or r - l + 1 < len(best):
                        best = s[l:r + 1]

                    tcount[get_index(s[l])] += 1
                    if tcount[get_index(s[l])] > 0:
                        have -= 1
                    l += 1
            r += 1
        return best or ""
                



            
        