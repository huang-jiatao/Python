import os


def test():

    print('计算BMI')
    h = float(input('请输入身高/cm：'))
    w = float(input('请输入体重/kg:'))
    bmi = (w) / ((h / 100)**2)
    print('你的身高是' + str(h) + 'cm,你的体重是' + str(w) + 'kg,你的BMI指数是：' + str(bmi))
    if bmi < 18.5:
        print('你的体重过轻')
    elif bmi >= 18.5 and bmi < 25:
        print('你的BMI指数正常，请好好保持！')
    elif bmi >= 25 and bmi < 28:
        print('你有那么一点点过重了，请加强锻炼。')
    elif bmi >= 28 and bmi < 32:
        print('额，你一定是个吃货吧？你的BMI过高，请注意身体健康！')
    elif bmi > 32:
        print('wow！大神，你真的不能再吃了！')


def main():
    test()


if __name__ == '__main__':
    main()
