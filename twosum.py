def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # ��len()����ȡ��nums�б�ĳ���
    n = len(nums)
    # xȡֵ��0һֱ��n��������n��
    for x in range(n):
        # yȡֵ��x+1һֱ��n��������n��
        # ��x+1�Ǽ��ٲ���Ҫ��ѭ��,y��ȡֵ�϶��Ǳ�x��
        for y in range(x + 1, n):
            # ���� target-nums[x]��ĳ��ֵ������nums��
            if nums[y] == target - nums[x]:
                # ����x��y
                return x, y
                break
            else:
                continue
