import os


def test():

    print('����BMI')
    h = float(input('���������/cm��'))
    w = float(input('����������/kg:'))
    bmi = (w) / ((h / 100)**2)
    print('��������' + str(h) + 'cm,���������' + str(w) + 'kg,���BMIָ���ǣ�' + str(bmi))
    if bmi < 18.5:
        print('������ع���')
    elif bmi >= 18.5 and bmi < 25:
        print('���BMIָ����������úñ��֣�')
    elif bmi >= 25 and bmi < 28:
        print('������ôһ�������ˣ����ǿ������')
    elif bmi >= 28 and bmi < 32:
        print('���һ���Ǹ��Ի��ɣ����BMI���ߣ���ע�����彡����')
    elif bmi > 32:
        print('wow����������Ĳ����ٳ��ˣ�')


def main():
    test()


if __name__ == '__main__':
    main()
