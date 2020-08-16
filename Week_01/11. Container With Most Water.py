# Moving Zeroes 上一题讲的是一维数组的坐标变换 i, j
# 本题也是关于一维数组的坐标变换，本题两种解法的代码都要写很熟，是后面同类题目的基础
# 可能解法：
# 解法1：枚举法，双指针，嵌套循环，O(n^2)，但本题枚举法用python会超出时间限制
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
				# 以下嵌套循环当需要遍历左右边界，且左右边界不可重复时使用，也就是可以实现i, j两个下标对数组的遍历，同时保证i与j不重复；需要背熟！；
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                ans = max(area, ans)           
        return ans
# 解法2：双指针分别指向左右边界，并向中间收敛，又称为左右夹逼法（基础）
# 挡板之间盛水面积为：短板（高）*两板间距（底）；因为面积由短板决定，所以移动/缩窄长板无论其是变长还是变短，都不会使得面积变大。每次缩窄隔板间距（底）都会-1，如果其移动后比当前短板还短，那么面积更会缩小。因此只有移动/缩窄短板才有可能遇到更长的板，不仅弥补底-1的损失，更增大盛水面积。所以谁的高度更小谁就往里挪。超哥角度：从最左与最右隔板开始，宽度最宽，此时要获得更大面积，必须往中间收拢，寻找比当前短板更高的隔板。因为如果里面的隔板不及外部隔板高的话，那么宽度肯定也不及外部，因此面积也肯定不及外部。只有一层循环：O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
				# 双指针分别指向首尾隔板
        l, r = 0, len(height) - 1
        ans = 0 
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(area, ans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans