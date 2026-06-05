class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Format: <length 0-9><delimiter |><string>...
        """
        return "".join([f"{"0" * (3 - len(str(len(s)))) + str(len(s))}{s}" for s in strs])


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            # parse start
            curr_num = s[i:i+3]
            start = i + 3
            end = start + int(curr_num)
            result.append(s[start:end])
            curr_num = ""
            i = end
        return result
            

