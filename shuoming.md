1. 前言
之前在查普通话成绩的时候，发现需要只名字和身份证就能查到用户的的证件照

在学校的网站上，学生信息经常会被公开，比如四六级考试，或者防护性做的比较差的教务管理系统，很容易就能拿到同学的信息，于是我用爬虫爬拿到了学校一部分同学的证件信息

2. 环境准备
chrome
python 3
requests 网络库
os 本地存储
urllib.request 下载图片
json 临时存储数据
time 计算爬虫时间
普通话成绩查询网址：http://www.cltt.org/studentscore
3. 分析
打开F12开发者工具，观察到我们的表单数据通过post方式，提交给了/StudentScore/ScoreResult，post请求提交了三个数据name,?stuID,?idCard，于是我们就可以使用requests 来模拟发送post请求了。
4. 代码
4.1 爬取照片地址
首先，我已经通过爬虫拿到了学生的信息并保存到了本地
所以直接从本地读取json得到学生对象

def get_stu_list(path):
    with open(path, 'r', encoding='utf-8') as f:
        stu_list = json.load(f)
    return stu_list
然后请求网站得到照片的地址，做了一些异常处理，因为有些同学可能没有去参加这个考试
def get_image_url(name, id):
    if not name or not id:
        return ""
    url = 'http://www.cltt.org/StudentScore/ScoreResult'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36'
    }
    data = {
        'name': name,
        'idCard': id
    }
    try:
        res = requests.post(url, data=data, headers=headers).text
    except requests.ConnectionError:
        print(name + '查询异常')
        return ""

    doc = PyQuery(res)
    img_src = doc('.user-img').find('img').attr('src')
    if not img_src:
        return ""
    else:
        return img_src
然后通过学生数组，循环调用get_image_url，我们就可以拿到所有的照片地址

4.2 给图片分类保存到本地
拿到照片地址之后，我们使用urlretrieve方法来下载图片

使用os.markdirs方法来创建文件夹并给图片分类

def get_stu_list(path):
    with open(path, 'r', encoding='utf-8') as f:
        stu_list = json.load(f)
    for stu in stu_list:
        if not stu['img']:
            continue
        college = stu['college']
        stu_class = stu['class']
        directory = college + '/' + stu_class
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = '{}/{}/{}.jpeg'.format(college, stu_class, stu['name'])
        urlretrieve(stu['img'], filename=filename)
    return stu_list

