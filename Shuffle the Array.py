Another simple 3 line python code to solve it in O(1) space:
for i in range(n):
            nums[ 2 * i + 1 : 2 * i + 1 ]=[nums.pop( n + i )]
        return nums
Here, nums[i:i] inserts any iterable (e.g. [2]) at ith index by shifting the rest of the elements right.
However bit operations are computationally much more efficient, whereas here we have to shift elements to insert other elements.
