def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    merged = []
    idx1 = 0
    idx2 = 0
    while (idx1 + idx2) < len(nums1):
        if idx1 < m and nums1[idx1] <= nums2[idx2]:
            merged.append(nums1[idx1])
            idx1 += 1
        else:
            merged.append(nums2[idx2])
            idx2 += 1
    nums1 = merged
    print(nums1)


a = [1, 2, 3, 0, 0, 0]
b = 3
c = [2, 5, 6]
d = 3
merge(a, b, c, d)
