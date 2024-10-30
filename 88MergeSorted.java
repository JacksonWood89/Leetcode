class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] merged = new int[m + n];
        int idx1 = 0;
        int idx2 = 0;
        while ((idx1 + idx2) < (m + n)) {
            if (n > 0) {
                if (idx1 <= m && nums1[idx1] <= nums2[idx2]) {
                    merged[idx1 + idx2] = nums1[idx1];
                    idx1++;
                } else {
                    merged[idx1 + idx2] = nums2[idx2];
                    idx2++;
                }
            } else {
                idx1 += n;
                idx2 += m;
            }
        }
        nums1 = merged;
    }
}