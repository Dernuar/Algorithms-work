class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        val = 0
        if low<=root.val<=high:
            val+=root.val
        val += self.rangeSumBST(root.left, low, high)
        val += self.rangeSumBST(root.right, low, high)

        return val