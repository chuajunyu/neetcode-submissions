class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the shorter array
        shorter = nums1 if len(nums1) <= len(nums2) else nums2
        longer = nums1 if shorter is not nums1 else nums2

        total = len(nums1) + len(nums2)

        # This is the index of the first median value
        half = total // 2

        # binary search the shorter array
        l, r = 0, len(shorter) - 1
        while True:
            m = (l + r) // 2

            # index of the remainder, - 2 to ensure indexes work
            j = half - m - 2
            print(j)

            # This is left of the partition, so there should be half of the elements here
            shorter_left = shorter[m] if m >= 0 else -1
            longer_left = longer[j] if j >= 0 else -1

            # this is right of the partition, half of the elements here, + 1 if odd
            shorter_right = shorter[m + 1] if (m + 1) < len(shorter) else 1000000000
            longer_right = longer[j + 1] if (j + 1) < len(longer) else 1000000000

            if shorter_left <= longer_right and longer_left <= shorter_right:
                if total % 2:  # if odd
                    return min(shorter_right, longer_right) 
                return (max(shorter_left, longer_left) + min(shorter_right, longer_right)) / 2
            elif shorter_left > longer_right:
                r = m - 1
            else:
                l = m + 1




            

            
        