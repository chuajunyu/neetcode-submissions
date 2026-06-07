class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # convert s1 into a binary array
        string_rep = [0] * 26
        for c in s1:
            string_rep[ord(c) - ord('a')] += 1
        
        print(string_rep)

        # load initial sliding window
        for i in range(len(s1)):
            string_rep[ord(s2[i]) - ord('a')] -= 1
        
        if not any(string_rep):
            return True

        # test all windows
        for i in range(len(s1), len(s2)):
            string_rep[ord(s2[i]) - ord('a')] -= 1
            string_rep[ord(s2[i - len(s1)]) - ord('a')] += 1
            if not any(string_rep):
                return True
        
        return False
        