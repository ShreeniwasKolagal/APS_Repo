class SegmentTree:
    def __init__(self, arr):
        """
        arr: list of numbers
        Builds a segment tree to answer range-sum queries in O(log n).
        """
        self.n = len(arr)
        # Next power-of-2 size
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        # Initialize tree array of length 2*size
        self.tree = [0] * (2 * size)

        # Build leaves
        for i in range(self.n):
            self.tree[size + i] = arr[i]
        # Build internal nodes
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx, value):
        """
        Point‐update: set arr[idx] = value
        """
        i = idx + self.size
        self.tree[i] = value
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def range_sum(self, left, right):
        """
        Query sum on interval [left, right] (0-based, inclusive)
        """
        res = 0
        l = left + self.size
        r = right + self.size
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res


# Example:
arr = [2, 1, 5, 3, 4]
st = SegmentTree(arr)
print(st.range_sum(1, 3))  # sum of arr[1..3] = 1+5+3 = 9
st.update(2, 10)          # arr[2] = 10
print(st.range_sum(1, 3))  # now 1 + 10 + 3 = 14
