class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Format: <length 0-9><delimiter |><string>...
        """
        return "".join([f"{str(len(s))}|{s}" for s in strs])


    def decode(self, s: str) -> List[str]:
        curr_num = ""
        i = 0
        result = []
        while i < len(s):
            # parse start
            if s[i] in "0123456789":
                curr_num += s[i]
                i += 1
            elif s[i] == "|":
                start = i + 1
                end = start + int(curr_num)
                result.append(s[start:end])
                curr_num = ""
                i = end
        return result
            

