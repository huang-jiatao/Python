class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = list(str(x))
        i, j = 0, len(str_x) - 1
        while i < j:
            if str_x[i] != str_x[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    is_int = s.isPalindrome(121)
    print(is_int)
