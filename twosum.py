def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 用len()方法取得nums列表的长度
    n = len(nums)
    # x取值从0一直到n（不包括n）
    for x in range(n):
        # y取值从x+1一直到n（不包括n）
        # 用x+1是减少不必要的循环,y的取值肯定是比x大
        for y in range(x + 1, n):
            # 假如 target-nums[x]的某个值存在于nums中
            if nums[y] == target - nums[x]:
                # 返回x和y
                return x, y
                break
            else:
                continue
