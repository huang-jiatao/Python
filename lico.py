class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # �ж��Ƿ�Ϊ��λ�����Ǹ�λ�����÷�ת��ֱ�ӷ���
        if -10 < x < 10:
            return x
        # ������xתΪ�ַ���
        str_x = str(x)
        # �жϵ�һ���Ƿ�Ϊ����
        if str_x[0] != "-":
            # ���Ǹ�����ֱ�ӷ�ת
            str_x = str_x[::-1]
            # strתΪint
            x = int(str_x)
        else:
            # �Ǹ��ţ���ת����֮����ַ���
            str_x = str_x[1:][::-1]
            # strתint
            x = int(str_x)
            # ���ϸ���
            x = -x
        # ��Ŀ��������ж��Ƿ����
        # ���-2147483648 < x < 2147483647�򷵻�x�����򷵻�0
        return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)
